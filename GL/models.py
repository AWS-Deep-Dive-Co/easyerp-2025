from django.db import models
import uuid

# Create your models here.
class Account(models.Model):
    AccountName = models.CharField(max_length=250)
    AccountNumber = models.CharField(max_length=20)
    BalanceType = models.CharField(max_length=20)
    Balance =  models.FloatField(default=0)

    def __str__(self):
          return self.AccountName

class JournalEntryHeader(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    Description = models.CharField(max_length=250)

    
class JournalEntryDetail(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    Account = models.ForeignKey(Account, on_delete=models.CASCADE)
    DebitOrCredit = models.CharField(max_length=250)
    Amount =  models.FloatField(default=0)