from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TicketType(models.Model):
    """Dynamic ticket types that can be managed through admin"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('pending_approval', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('closed', 'Closed'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]
    
    # Basic ticket information
    ticket_number = models.CharField(max_length=20, unique=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    
    # People involved
    requested_by = models.CharField(max_length=200, help_text="Name of person who requested this")
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tickets')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    # Additional fields
    business_justification = models.TextField(blank=True, help_text="Business justification for this request")
    technical_details = models.TextField(blank=True, help_text="Technical implementation details")
    risk_assessment = models.TextField(blank=True, help_text="Risk assessment and mitigation")
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.ticket_number} - {self.title}"
    
    def save(self, *args, **kwargs):
        if not self.ticket_number:
            # Generate ticket number: TIC-YYYYMMDD-XXXX
            today = timezone.now().strftime('%Y%m%d')
            latest_ticket = Ticket.objects.filter(
                ticket_number__startswith=f'TIC-{today}'
            ).order_by('-ticket_number').first()
            
            if latest_ticket:
                latest_num = int(latest_ticket.ticket_number.split('-')[-1])
                new_num = latest_num + 1
            else:
                new_num = 1
            
            self.ticket_number = f'TIC-{today}-{new_num:04d}'
        
        super().save(*args, **kwargs)


class TicketApproval(models.Model):
    """Track multiple approvals for tickets (especially change requests)"""
    APPROVAL_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='approvals')
    approver_name = models.CharField(max_length=200, help_text="Name of the approver")
    approver_title = models.CharField(max_length=200, blank=True, help_text="Title/Role of the approver")
    status = models.CharField(max_length=20, choices=APPROVAL_STATUS_CHOICES, default='pending')
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['created_at']
        unique_together = ['ticket', 'approver_name']
    
    def __str__(self):
        return f"{self.ticket.ticket_number} - {self.approver_name} ({self.status})"
    
    def save(self, *args, **kwargs):
        if self.status in ['approved', 'rejected'] and not self.approved_at:
            self.approved_at = timezone.now()
        super().save(*args, **kwargs)


class TicketComment(models.Model):
    """Comments and updates on tickets"""
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    is_internal = models.BooleanField(default=False, help_text="Internal comment (not visible to requestor)")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"{self.ticket.ticket_number} - Comment by {self.author.username}"


class TicketAttachment(models.Model):
    """File attachments for tickets"""
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='ticket_attachments/')
    filename = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['uploaded_at']
    
    def __str__(self):
        return f"{self.ticket.ticket_number} - {self.filename}"
