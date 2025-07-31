from django import forms
from django.contrib.auth.models import User
from .models import Ticket, TicketType, TicketApproval, TicketComment


class TicketForm(forms.ModelForm):
    approvers = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        required=False,
        help_text="Enter approvers, one per line. Format: 'Name | Title' or just 'Name'"
    )
    
    class Meta:
        model = Ticket
        fields = [
            'title', 'description', 'ticket_type', 'status', 'priority',
            'requested_by', 'assigned_to', 'due_date', 
            'business_justification', 'technical_details', 'risk_assessment'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
            'business_justification': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
            'technical_details': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
            'risk_assessment': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ticket_type'].queryset = TicketType.objects.filter(is_active=True)


class TicketSearchForm(forms.Form):
    search = forms.CharField(
        max_length=200, 
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search tickets...',
            'class': 'form-control'
        })
    )
    ticket_type = forms.ModelChoiceField(
        queryset=TicketType.objects.filter(is_active=True),
        required=False,
        empty_label="All Types",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    status = forms.ChoiceField(
        choices=[('', 'All Statuses')] + Ticket.STATUS_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    priority = forms.ChoiceField(
        choices=[('', 'All Priorities')] + Ticket.PRIORITY_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class TicketApprovalForm(forms.ModelForm):
    class Meta:
        model = TicketApproval
        fields = ['status', 'comments']
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
        }


class TicketCommentForm(forms.ModelForm):
    class Meta:
        model = TicketComment
        fields = ['comment', 'is_internal']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }
