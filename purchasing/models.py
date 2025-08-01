# Purchasing Management Models
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from inventory.models import Product, Supplier
import uuid

User = get_user_model()

class PurchaseOrder(models.Model):
    """Purchase Order header"""
    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('SENT', 'Sent to Supplier'),
        ('CONFIRMED', 'Confirmed'),
        ('RECEIVED', 'Received'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    po_number = models.CharField(max_length=50, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_date = models.DateField(default=timezone.now)
    required_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_pos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.po_number} - {self.supplier.name}"

    class Meta:
        ordering = ['-created_at']

class PurchaseOrderLine(models.Model):
    """Purchase Order line items"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='lines')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_ordered = models.IntegerField()
    quantity_received = models.IntegerField(default=0)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calculate line total
        self.line_total = self.quantity_ordered * self.unit_cost
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.purchase_order.po_number} - {self.product.name}"

    @property
    def quantity_pending(self):
        return self.quantity_ordered - self.quantity_received

class GoodsReceipt(models.Model):
    """Goods Receipt/Receiving documents"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    receipt_number = models.CharField(max_length=50, unique=True)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    received_date = models.DateField(default=timezone.now)
    received_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.receipt_number} - {self.purchase_order.po_number}"

    class Meta:
        ordering = ['-created_at']

class GoodsReceiptLine(models.Model):
    """Goods Receipt line items"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    goods_receipt = models.ForeignKey(GoodsReceipt, on_delete=models.CASCADE, related_name='lines')
    purchase_order_line = models.ForeignKey(PurchaseOrderLine, on_delete=models.CASCADE)
    quantity_received = models.IntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.goods_receipt.receipt_number} - {self.purchase_order_line.product.name}"
