from django.contrib import admin

from tenant_management.app.models.tenant import Tenant


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")


