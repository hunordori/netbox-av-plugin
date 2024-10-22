from netbox.filtersets import NetBoxModelFilterSet
from .models import AV, AVInterface


class AVFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = AV
        fields = ['name', ]

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)


class AVInterfaceFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = AVInterface
        fields = ['name', "medium", "videorate", "direction"]

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)