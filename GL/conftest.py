import pytest
from mixer.backend.django import mixer


@pytest.fixture
def make_fiscal_year():
    def _make_fiscal_year(**overrides):
        return mixer.blend("GL.FiscalYear", **overrides)

    return _make_fiscal_year


@pytest.fixture
def make_account_type():
    def _make_account_type(**overrides):
        return mixer.blend("GL.AccountType", **overrides)

    return _make_account_type


@pytest.fixture
def make_account(make_account_type):
    def _make_account(**overrides):
        overrides.setdefault("account_type", make_account_type())
        return mixer.blend("GL.Account", **overrides)

    return _make_account
