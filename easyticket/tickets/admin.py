from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.html import format_html
from django.views.decorators.csrf import csrf_exempt
import csv
import json
from .models import TicketType, Ticket, TicketApproval, TicketComment, TicketAttachment


class TicketApprovalInline(admin.TabularInline):
    model = TicketApproval
    extra = 1
    readonly_fields = ('approved_at',)


class TicketCommentInline(admin.TabularInline):
    model = TicketComment
    extra = 1
    readonly_fields = ('created_at',)


class TicketAttachmentInline(admin.TabularInline):
    model = TicketAttachment
    extra = 1
    readonly_fields = ('uploaded_at',)


@admin.register(TicketType)
class TicketTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('is_active',)
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('bulk-manage/', self.admin_site.admin_view(self.bulk_manage_view), name='tickets_tickettype_bulk_manage'),
        ]
        return custom_urls + urls
    
    def bulk_manage_view(self, request):
        if request.method == 'POST':
            if 'bulk_create' in request.POST:
                types_text = request.POST.get('types_text', '')
                created_count = 0
                
                for line in types_text.strip().split('\n'):
                    line = line.strip()
                    if line:
                        if '|' in line:
                            name, description = line.split('|', 1)
                            name = name.strip()
                            description = description.strip()
                        else:
                            name = line
                            description = ''
                        
                        if not TicketType.objects.filter(name=name).exists():
                            TicketType.objects.create(name=name, description=description)
                            created_count += 1
                
                messages.success(request, f'Created {created_count} new ticket types.')
                return redirect('admin:tickets_tickettype_changelist')
        
        return render(request, 'admin/tickets/tickettype/bulk_manage.html')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'title', 'ticket_type', 'status', 'priority', 'requested_by', 'created_at')
    list_filter = ('status', 'priority', 'ticket_type', 'created_at')
    search_fields = ('ticket_number', 'title', 'description', 'requested_by')
    readonly_fields = ('ticket_number', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('ticket_number', 'title', 'description', 'ticket_type', 'status', 'priority')
        }),
        ('People', {
            'fields': ('requested_by', 'assigned_to', 'created_by')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at', 'due_date', 'resolved_at')
        }),
        ('Additional Details', {
            'fields': ('business_justification', 'technical_details', 'risk_assessment'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [TicketApprovalInline, TicketCommentInline, TicketAttachmentInline]
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('export/', self.admin_site.admin_view(self.export_tickets), name='tickets_ticket_export'),
            path('import/', self.admin_site.admin_view(self.import_tickets), name='tickets_ticket_import'),
        ]
        return custom_urls + urls
    
    def export_tickets(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="tickets_export.csv"'
        
        writer = csv.writer(response)
        writer.writerow([
            'Ticket Number', 'Title', 'Description', 'Type', 'Status', 'Priority',
            'Requested By', 'Assigned To', 'Created By', 'Created At', 'Due Date',
            'Business Justification', 'Technical Details', 'Risk Assessment'
        ])
        
        for ticket in Ticket.objects.all():
            writer.writerow([
                ticket.ticket_number,
                ticket.title,
                ticket.description,
                ticket.ticket_type.name,
                ticket.status,
                ticket.priority,
                ticket.requested_by,
                ticket.assigned_to.username if ticket.assigned_to else '',
                ticket.created_by.username,
                ticket.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                ticket.due_date.strftime('%Y-%m-%d %H:%M:%S') if ticket.due_date else '',
                ticket.business_justification,
                ticket.technical_details,
                ticket.risk_assessment,
            ])
        
        return response
    
    def import_tickets(self, request):
        if request.method == 'POST' and request.FILES.get('csv_file'):
            csv_file = request.FILES['csv_file']
            try:
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(decoded_file)
                
                imported_count = 0
                for row in reader:
                    # Basic validation
                    if not row.get('Title') or not row.get('Type'):
                        continue
                    
                    # Get or create ticket type
                    ticket_type, _ = TicketType.objects.get_or_create(
                        name=row['Type'],
                        defaults={'description': f'Auto-created from import'}
                    )
                    
                    # Create ticket (skip if ticket number already exists)
                    if row.get('Ticket Number') and Ticket.objects.filter(ticket_number=row['Ticket Number']).exists():
                        continue
                    
                    ticket = Ticket(
                        title=row['Title'],
                        description=row.get('Description', ''),
                        ticket_type=ticket_type,
                        status=row.get('Status', 'open'),
                        priority=row.get('Priority', 'medium'),
                        requested_by=row.get('Requested By', 'Unknown'),
                        created_by=request.user,
                        business_justification=row.get('Business Justification', ''),
                        technical_details=row.get('Technical Details', ''),
                        risk_assessment=row.get('Risk Assessment', ''),
                    )
                    ticket.save()
                    imported_count += 1
                
                messages.success(request, f'Successfully imported {imported_count} tickets.')
                return redirect('admin:tickets_ticket_changelist')
                
            except Exception as e:
                messages.error(request, f'Error importing tickets: {str(e)}')
        
        return render(request, 'admin/tickets/ticket/import.html')
    
    def save_model(self, request, obj, form, change):
        if not change:  # Creating new ticket
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(TicketApproval)
class TicketApprovalAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'approver_name', 'approver_title', 'status', 'created_at', 'approved_at')
    list_filter = ('status', 'created_at', 'approved_at')
    search_fields = ('ticket__ticket_number', 'approver_name', 'approver_title')
    readonly_fields = ('approved_at',)


@admin.register(TicketComment)
class TicketCommentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'author', 'is_internal', 'created_at')
    list_filter = ('is_internal', 'created_at')
    search_fields = ('ticket__ticket_number', 'comment')
    readonly_fields = ('created_at',)


@admin.register(TicketAttachment)
class TicketAttachmentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'filename', 'uploaded_by', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('ticket__ticket_number', 'filename')
    readonly_fields = ('uploaded_at',)
