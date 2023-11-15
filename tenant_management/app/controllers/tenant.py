from django.core.management import call_command
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from tenant_management.app.models.employee import Employee
from tenant_management.app.serializers.tenant import TenantSerializer
from tenant_management.app.utils.middlewares import set_custom_schema


class EmployeeListCreateAPIView(APIView, LimitOffsetPagination):
    def get(self, request):
        final_result = []

        # Set schema to Rohit
        set_custom_schema(request, "rohit")
        rohit_qs = Employee.objects.all()
        final_result.append(TenantSerializer(rohit_qs, many=True).data)

        # Set schema to Abhishek
        set_custom_schema(request, "abhi")
        abhishek_qs = Employee.objects.all()
        final_result.append(TenantSerializer(abhishek_qs, many=True).data)

        # Set schema to Rohit
        set_custom_schema(request, "rohit")
        rohit_qs = Employee.objects.all()
        final_result.append(TenantSerializer(rohit_qs, many=True).data)

        return Response(final_result)

    @staticmethod
    def post(request):
        set_custom_schema(request, "public")
        name = "rohitd"
        call_command(
            "create_tenant",
            verbosity=0,
            interactive=False,
            schema_name=f"{name}",
            domain_domain=f"{name}.com",
            name=f"{name}",
        )
        return Response({"status": "success"}, status=status.HTTP_201_CREATED)


class TenantRetrieveUpdateDeleteAPIView(APIView):
    @staticmethod
    def get(request, pk):
        tenant = get_object_or_404(Employee, pk=pk)
        serializer = TenantSerializer(tenant)
        return Response(serializer.data)

    @staticmethod
    def put(request, pk):
        tenant = get_object_or_404(Employee, pk=pk)
        serializer = TenantSerializer(tenant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        tenant = get_object_or_404(Employee, pk=pk)
        tenant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
