from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Ticket, TicketType, TicketApproval, TicketComment
from .forms import TicketForm, TicketSearchForm, TicketApprovalForm, TicketCommentForm


def ticket_list(request):
    """Public view to list and search tickets"""
    form = TicketSearchForm(request.GET)
    tickets = Ticket.objects.select_related('ticket_type', 'created_by', 'assigned_to').prefetch_related('approvals')
    
    if form.is_valid():
        search_query = form.cleaned_data.get('search')
        ticket_type = form.cleaned_data.get('ticket_type')
        status = form.cleaned_data.get('status')
        priority = form.cleaned_data.get('priority')
        
        if search_query:
            tickets = tickets.filter(
                Q(ticket_number__icontains=search_query) |
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(requested_by__icontains=search_query)
            )
        
        if ticket_type:
            tickets = tickets.filter(ticket_type=ticket_type)
        
        if status:
            tickets = tickets.filter(status=status)
        
        if priority:
            tickets = tickets.filter(priority=priority)
    
    paginator = Paginator(tickets, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'form': form,
        'page_obj': page_obj,
        'tickets': page_obj,
    }
    return render(request, 'tickets/ticket_list.html', context)


def ticket_detail(request, ticket_number):
    """Public view to view ticket details"""
    ticket = get_object_or_404(
        Ticket.objects.select_related('ticket_type', 'created_by', 'assigned_to')
                     .prefetch_related('approvals', 'comments__author', 'attachments'),
        ticket_number=ticket_number
    )
    
    # Filter out internal comments for non-authenticated users
    comments = ticket.comments.all()
    if not request.user.is_authenticated:
        comments = comments.filter(is_internal=False)
    
    context = {
        'ticket': ticket,
        'comments': comments,
    }
    return render(request, 'tickets/ticket_detail.html', context)


@login_required
def ticket_create(request):
    """Admin-only view to create tickets"""
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            
            # Create approval entries if this is a change request
            approvers = form.cleaned_data.get('approvers', '')
            if approvers:
                for approver_line in approvers.strip().split('\n'):
                    approver_line = approver_line.strip()
                    if approver_line:
                        if '|' in approver_line:
                            name, title = approver_line.split('|', 1)
                            name = name.strip()
                            title = title.strip()
                        else:
                            name = approver_line
                            title = ''
                        
                        TicketApproval.objects.create(
                            ticket=ticket,
                            approver_name=name,
                            approver_title=title
                        )
            
            messages.success(request, f'Ticket {ticket.ticket_number} created successfully.')
            return redirect('ticket_detail', ticket_number=ticket.ticket_number)
    else:
        form = TicketForm()
    
    return render(request, 'tickets/ticket_create.html', {'form': form})


@login_required
def ticket_edit(request, ticket_number):
    """Admin-only view to edit tickets"""
    ticket = get_object_or_404(Ticket, ticket_number=ticket_number)
    
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ticket {ticket.ticket_number} updated successfully.')
            return redirect('ticket_detail', ticket_number=ticket.ticket_number)
    else:
        form = TicketForm(instance=ticket)
    
    return render(request, 'tickets/ticket_edit.html', {'form': form, 'ticket': ticket})


@login_required
def ticket_add_comment(request, ticket_number):
    """Admin-only view to add comments"""
    ticket = get_object_or_404(Ticket, ticket_number=ticket_number)
    
    if request.method == 'POST':
        form = TicketCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = ticket
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully.')
            return redirect('ticket_detail', ticket_number=ticket.ticket_number)
    else:
        form = TicketCommentForm()
    
    return render(request, 'tickets/ticket_add_comment.html', {
        'form': form, 
        'ticket': ticket
    })


@login_required
def approval_update(request, approval_id):
    """Admin-only view to update approval status"""
    approval = get_object_or_404(TicketApproval, id=approval_id)
    
    if request.method == 'POST':
        form = TicketApprovalForm(request.POST, instance=approval)
        if form.is_valid():
            form.save()
            messages.success(request, f'Approval status updated for {approval.approver_name}.')
            return redirect('ticket_detail', ticket_number=approval.ticket.ticket_number)
    else:
        form = TicketApprovalForm(instance=approval)
    
    return render(request, 'tickets/approval_update.html', {
        'form': form, 
        'approval': approval
    })


def dashboard(request):
    """Dashboard with ticket statistics"""
    total_tickets = Ticket.objects.count()
    open_tickets = Ticket.objects.filter(status='open').count()
    pending_approval = Ticket.objects.filter(status='pending_approval').count()
    critical_tickets = Ticket.objects.filter(priority='critical').count()
    
    # Recent tickets
    recent_tickets = Ticket.objects.select_related('ticket_type')[:10]
    
    # Tickets by type
    type_stats = {}
    for ticket_type in TicketType.objects.filter(is_active=True):
        type_stats[ticket_type.name] = Ticket.objects.filter(ticket_type=ticket_type).count()
    
    context = {
        'total_tickets': total_tickets,
        'open_tickets': open_tickets,
        'pending_approval': pending_approval,
        'critical_tickets': critical_tickets,
        'recent_tickets': recent_tickets,
        'type_stats': type_stats,
    }
    return render(request, 'tickets/dashboard.html', context)
