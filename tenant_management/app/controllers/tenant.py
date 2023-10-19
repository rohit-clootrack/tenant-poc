from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from tenant_management.app.models.tenant import Tenant
from tenant_management.app.serializers.tenant import TenantSerializer


class TenantListCreateAPIView(APIView, LimitOffsetPagination):
    def get(self, request):
        tenants_qs = Tenant.objects.all()
        page = self.paginate_queryset(tenants_qs, request, view=self)
        if page is not None:
            serializer = TenantSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        # Return all the items
        serializer = TenantSerializer(tenants_qs, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = TenantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TenantRetrieveUpdateDeleteAPIView(APIView):
    @staticmethod
    def get(request, pk):
        tenant = get_object_or_404(Tenant, pk=pk)
        serializer = TenantSerializer(tenant)
        return Response(serializer.data)

    @staticmethod
    def put(request, pk):
        tenant = get_object_or_404(Tenant, pk=pk)
        serializer = TenantSerializer(tenant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        tenant = get_object_or_404(Tenant, pk=pk)
        tenant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
