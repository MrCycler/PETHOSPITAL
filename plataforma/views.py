from rest_framework import viewsets, filters, mixins, views, status
from rest_framework.serializers import Serializer
from .models import Client, Pet, Doctor
from .serializers import ClientSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ClientViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter) # filter por defecto
    ordering_fields = ('created_at',)