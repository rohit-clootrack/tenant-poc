from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tenant_management.app.models.employee import Tenant


class TenantModelTestCase(TestCase):
    def test_tenant_creation(self):
        tenant = Tenant.objects.create(first_name="John", last_name="Doe")
        self.assertEqual(tenant.first_name, "John")
        self.assertEqual(tenant.last_name, "Doe")


class TenantAPITestCase(APITestCase):
    def setUp(self):
        self.tenant_data = {
            "first_name": "Alice",
            "last_name": "Johnson",
            "email": "alice@gmail.com",
        }

    def test_create_tenant(self):
        url = reverse("tenants")
        response = self.client.post(url, self.tenant_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tenant.objects.count(), 1)

    def test_list_tenants(self):
        Tenant.objects.create(first_name="Bobby", last_name="Smith")
        url = reverse("tenants")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assuming you have more than one tenant in the database
        self.assertGreater(len(response.data), 0)

    def test_retrieve_tenant(self):
        tenant = Tenant.objects.create(first_name="Bob", last_name="Smith")
        url = reverse("tenant", args=[tenant.id])  # Replace with the correct URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "Bob")

    def test_update_tenant(self):
        tenant = Tenant.objects.create(
            first_name="Charlie", last_name="Brown", email="charlie@gmail.com"
        )
        url = reverse("tenant", args=[tenant.id])
        updated_data = {"first_name": "David", "last_name": "Smith", "email": "david@gmail.com"}
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tenant.objects.get(id=tenant.id).first_name, "David")

    def test_delete_tenant(self):
        tenant = Tenant.objects.create(first_name="Eve", last_name="Johnson")
        url = reverse("tenant", args=[tenant.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tenant.objects.filter(id=tenant.id).count(), 0)
