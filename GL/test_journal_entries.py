"""Real tests for GL business logic (see root CLAUDE.md for why this matters).

Replaces the old GL/test_file.py placeholder mock tests.
"""
from decimal import Decimal

import pytest
from django.db import IntegrityError
from mixer.backend.django import mixer

from GL.models import JournalEntryHeader, JournalEntryDetail, Account, FinancialPeriod

pytestmark = pytest.mark.django_db


class TestJournalEntryIsBalanced:
    def test_is_balanced_true_when_debits_equal_credits(self, make_fiscal_year):
        entry = mixer.blend(
            JournalEntryHeader,
            fiscal_year=make_fiscal_year(),
            total_debit=Decimal("1000.00"),
            total_credit=Decimal("1000.00"),
        )
        assert entry.is_balanced is True

    def test_is_balanced_false_when_debits_and_credits_differ(self, make_fiscal_year):
        entry = mixer.blend(
            JournalEntryHeader,
            fiscal_year=make_fiscal_year(),
            total_debit=Decimal("1000.00"),
            total_credit=Decimal("900.00"),
        )
        assert entry.is_balanced is False


class TestJournalEntryDetailReconciliation:
    def test_detail_lines_sum_to_header_totals(self, make_fiscal_year, make_account):
        entry = mixer.blend(
            JournalEntryHeader,
            fiscal_year=make_fiscal_year(),
            total_debit=Decimal("500.00"),
            total_credit=Decimal("500.00"),
        )
        mixer.blend(
            JournalEntryDetail,
            journal_entry=entry,
            account=make_account(),
            debit_amount=Decimal("300.00"),
            credit_amount=Decimal("0.00"),
        )
        mixer.blend(
            JournalEntryDetail,
            journal_entry=entry,
            account=make_account(),
            debit_amount=Decimal("200.00"),
            credit_amount=Decimal("0.00"),
        )
        mixer.blend(
            JournalEntryDetail,
            journal_entry=entry,
            account=make_account(),
            debit_amount=Decimal("0.00"),
            credit_amount=Decimal("500.00"),
        )

        lines = entry.lines.all()
        debit_sum = sum(line.debit_amount for line in lines)
        credit_sum = sum(line.credit_amount for line in lines)

        assert debit_sum == entry.total_debit
        assert credit_sum == entry.total_credit
        assert entry.is_balanced


class TestAccountHierarchy:
    def test_account_can_reference_parent_account(self, make_account):
        parent = make_account(account_number="1000", account_name="Assets", is_header=True)
        child = make_account(account_number="1010", account_name="Cash", parent_account=parent)

        assert child.parent_account == parent
        assert parent.account_set.filter(pk=child.pk).exists()

    def test_account_without_parent_is_valid(self, make_account):
        account = make_account(parent_account=None)
        assert account.parent_account is None


class TestFinancialPeriodUniqueness:
    def test_duplicate_period_for_same_fiscal_year_raises_integrity_error(self, make_fiscal_year):
        fiscal_year = make_fiscal_year()
        mixer.blend(
            FinancialPeriod,
            fiscal_year=fiscal_year,
            period_type="MONTHLY",
            period_number=1,
        )
        with pytest.raises(IntegrityError):
            mixer.blend(
                FinancialPeriod,
                fiscal_year=fiscal_year,
                period_type="MONTHLY",
                period_number=1,
            )
