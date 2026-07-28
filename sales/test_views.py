"""Smoke tests for sales' real (non-stub) list views: search + pagination."""
import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


@pytest.fixture
def logged_in_client(client, make_user):
    user = make_user()
    user.set_password("testpass123")
    user.save()
    client.force_login(user)
    return client


class TestCustomerListView:
    def test_requires_login(self, client):
        response = client.get("/sales/customers/")
        assert response.status_code == 302

    def test_lists_active_customers(self, logged_in_client, make_customer):
        make_customer(company_name="Acme Corp", is_active=True)
        make_customer(company_name="Zeta Industries", is_active=True)
        make_customer(company_name="Inactive Co", is_active=False)

        response = logged_in_client.get("/sales/customers/")

        assert response.status_code == 200
        names = [c.company_name for c in response.context["customers"]]
        assert "Acme Corp" in names
        assert "Zeta Industries" in names
        assert "Inactive Co" not in names

    def test_search_filters_by_company_name(self, logged_in_client, make_customer):
        make_customer(company_name="Acme Corp", is_active=True)
        make_customer(company_name="Zeta Industries", is_active=True)

        response = logged_in_client.get("/sales/customers/", {"search": "Acme"})

        names = [c.company_name for c in response.context["customers"]]
        assert names == ["Acme Corp"]


class TestSalesOrderListView:
    def test_requires_login(self, client):
        response = client.get("/sales/orders/")
        assert response.status_code == 302

    def test_filters_by_status(self, logged_in_client, make_customer):
        customer = make_customer()
        mixer.blend("sales.SalesOrder", customer=customer, status="DRAFT")
        mixer.blend("sales.SalesOrder", customer=customer, status="SHIPPED")

        response = logged_in_client.get("/sales/orders/", {"status": "DRAFT"})

        statuses = {o.status for o in response.context["orders"]}
        assert statuses == {"DRAFT"}
