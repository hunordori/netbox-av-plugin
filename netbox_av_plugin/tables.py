import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn

from .models import AVInterface


class AVInterfaceTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = AVInterface

        fields = ("pk", "id", "name", "enabled", "device", "videorate", "medium", "signaltype","direction", "comments", "tags")
        default_columns = ("name","medium", "device", "videorate", "medium")