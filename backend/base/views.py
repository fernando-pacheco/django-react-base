from rest_framework import viewsets

from .models import BaseIntModel, BaseUUIDModel
from .serializers import BaseIntSerializer, BaseUUIDSerializer


class BaseIntViewSet(viewsets.ModelViewSet):
    queryset = BaseIntModel.objects.all()
    serializer_class = BaseIntSerializer


class BaseUUIDViewSet(viewsets.ModelViewSet):
    queryset = BaseUUIDModel.objects.all()
    serializer_class = BaseUUIDSerializer
