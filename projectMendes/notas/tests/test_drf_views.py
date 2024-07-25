from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class TestPrivateCategoryViews:
    pass


class TestPublicCategoryViews:
    def test_get_category_fails_without_authentication(self):
        # Setup
        api_client = APIClient()
        view_url = reverse("nota-list")

        # Lógica
        response = api_client.get(view_url)

        # Validação
        assert response.status_code == status.HTTP_401_UNAUTHORIZED  # 401
