from django.db.models import Count

from dcim.models import Device, Interface
from netbox.views import generic
from utilities.views import ViewTab, register_model_view

from . import filtersets, forms, models, tables


class AVInterfaceView(generic.ObjectView):
    queryset = models.AVInterface.objects.all()

class AVInterfaceListView(generic.ObjectListView):
    queryset = models.AVInterface.objects.annotate(
        interface_count=Count('name')
    )
    table = tables.AVInterfaceTable

class AVInterfaceEditView(generic.ObjectEditView):
    queryset = models.AVInterface.objects.all()
    form = forms.AVInterfaceForm

class AVInterfaceDeleteView(generic.ObjectDeleteView):
    queryset = models.AVInterface.objects.all()

class AVInterfaceChildView(generic.ObjectChildrenView):
    """
    Defines the children view for AVInterfaces
    """

    child_model = models.AVInterface
    table = tables.AVInterfaceTable
    filterset = filtersets.AVInterfaceFilterSet
    template_name = "inc/view_tab.html"

    def get_extra_context(self, request, instance):
        return {
            "table_config": self.table.__name__,
            "model_type": self.queryset.model._meta.verbose_name.replace(" ", "_"),
            "add_url": "plugins:netbox_av_plugin:avinterface_add",
        }

    # def prep_table_data(self, request, queryset, parent):
    #     return queryset.annotate(
    #         rule_count=Count("name"),
    #     )

@register_model_view(Device, "access_lists")
class DeviceAVInterfaceView(AVInterfaceChildView):
    queryset = Device.objects.prefetch_related("tags")
    tab = ViewTab(
        label="AV Interface",
        badge=lambda obj: models.AVInterface.objects.filter(device=obj).count(),
        permission="netbox_av_plugin.view_accesslist",
    )

    def get_children(self, request, parent):
        return self.child_model.objects.restrict(request.user, "view").filter(
            device=parent,
        )