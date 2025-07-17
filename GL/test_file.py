from django.test import TestCase

# Create your tests here.
import pytest
from GL.models import Account    

@pytest.mark.django_db #give test access to database  
def test_account_create():    
    # Create dummy data       
    account = Account.objects.create(AccountName="Cash", AccountNumber="100-000-000",BalanceType='Debit',Balance=0.0,)  
    # Assert the dummy data saved as expected       
    assert account.AccountName=="Cash"      
    assert account.AccountNumber=="100-000-000"