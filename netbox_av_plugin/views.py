from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class AVView(generic.ObjectView):
    queryset = models.AV.objects.all()

class AVListView(generic.ObjectListView):
    queryset = models.AV.objects.all()
    table = tables.AVTable

class AVEditView(generic.ObjectEditView):
    queryset = models.AV.objects.all()
    form = forms.AVForm

class AVDeleteView(generic.ObjectDeleteView):
    queryset = models.AV.objects.all()



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