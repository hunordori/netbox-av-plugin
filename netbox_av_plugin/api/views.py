from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import AVInterfaceSerializer

class AVInterfaceViewSet(NetBoxModelViewSet):
    queryset = models.AVInterface.objects.prefetch_related('tags')
    serializer_class = AVInterfaceSerializer