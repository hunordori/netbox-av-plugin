import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn

from .models import AV, AVInterface


class AVTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = AV
        fields = ("pk", "id", "name", "actions")
        default_columns = ("name",)


class AVInterfaceTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = AVInterface
        fields = ("pk", "id", "name", "enabled", "device", "videorate", "medium", "direction", "comments", "tags")
        default_columns = ("name","medium", "type", "videorate", "medium")