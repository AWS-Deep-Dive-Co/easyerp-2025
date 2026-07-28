"""Real tests for the default app (see root CLAUDE.md for why this replaces the old mock tests)."""
import pytest
from mixer.backend.django import mixer

from default.models import User, Company

pytestmark = pytest.mark.django_db


class TestUserModel:
    def test_str_format(self):
        user = mixer.blend(User, first_name="Ada", last_name="Lovelace", username="ada")
        assert str(user) == "Ada Lovelace (ada)"

    def test_is_manager_defaults_to_false(self):
        user = mixer.blend(User)
        assert user.is_manager is False

    def test_employee_id_uniqueness_enforced(self):
        mixer.blend(User, employee_id="EMP-001")
        with pytest.raises(Exception):
            mixer.blend(User, employee_id="EMP-001")


class TestCompanyModel:
    def test_str_returns_name(self):
        company = mixer.blend(Company, name="Acme Corp")
        assert str(company) == "Acme Corp"


class TestHealthAndDashboardViews:
    def test_health_prefix_index_is_reachable(self, client):
        response = client.get("/health/")
        assert response.status_code == 200

    def test_dashboard_requires_login(self, client):
        response = client.get("/")
        assert response.status_code == 302

    def test_dashboard_renders_stats_for_logged_in_user(self, client):
        user = mixer.blend(User)
        client.force_login(user)

        response = client.get("/")

        assert response.status_code == 200
        assert response.context["modules_available"] is True
        assert "sales_stats" in response.context
        assert "gl_stats" in response.context
