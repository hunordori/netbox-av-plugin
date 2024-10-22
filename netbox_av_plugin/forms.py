from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from dcim.models import Device, Interface, Region, Site, SiteGroup

from .models import AV, AVInterface


class AVForm(NetBoxModelForm):
    class Meta:
        model = AV
        fields = ("name", "tags")

class AVInterfaceForm(NetBoxModelForm):
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
        query_params={
            "region_id": "$region",
            "group_id": "$site_group",
            "site_id": "$site",
        },
    )
    class Meta:
        model = AVInterface
        comments = CommentField()
        fields = ("name", "enabled", "device", "videorate", "medium", "direction", "comments", "tags")

class AVInterfaceFilterForm(NetBoxModelFilterSetForm):

    model = AVInterface
    videorate = forms.ModelMultipleChoiceField(
        queryset=AVInterface.objects.all(),
        required=False
    )