from django.db import connection
from django_tenants.middleware import TenantMainMiddleware
from django_tenants.postgresql_backend.base import FakeTenant


class CustomMiddleware(TenantMainMiddleware):
    @staticmethod
    def hostname_from_request(request):
        """Extracts hostname from request. Used for custom requests filtering.
        By default removes the request's port and common prefixes.
        """
        hostname = request.headers.get("X-Tenant-Id", None)
        return hostname

    def process_request(self, request):
        # Connection needs first to be at the public schema, as this is where
        # the tenant metadata is stored.

        hostname = self.hostname_from_request(request)
        if not hostname:
            from django.http import HttpResponseNotFound

            return HttpResponseNotFound()

        schema_name = hostname.split(".")[0]
        tenant = FakeTenant(tenant_type=None, schema_name=schema_name)
        tenant.domain_url = hostname
        request.tenant = tenant
        connection.set_tenant(request.tenant)
        self.setup_url_routing(request)
