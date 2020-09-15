from rest_framework import viewsets
from rest_framework import permissions as base_pm
from rest_framework import generics
from . import permissions
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models

# Create your views here.
class MyAccount(generics.ListAPIView):
    queryset = models.AccountProfile.objects.all()
    serializer_class = serializers.AccountSerializer
    permission_classes = [base_pm.IsAuthenticated, permissions.IsAccountOwner]

    def list(self, request):
        queryset = models.AccountProfile.objects.all().filter(id=request.user.id)
        serializer = serializers.AccountSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class Register(viewsets.ModelViewSet):
    serializer_class = serializers.AccountSerializer
    queryset = models.AccountProfile.objects.all()
    permission_classes = [base_pm.IsAdminUser]
