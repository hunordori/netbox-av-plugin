from netbox.filtersets import NetBoxModelFilterSet
from .models import AVInterface


class AVInterfaceFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = AVInterface
        fields = ['name', "medium", "videorate", "direction"]

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)