from netbox.filtersets import NetBoxModelFilterSet
from .models import AV


# class AVFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = AV
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
