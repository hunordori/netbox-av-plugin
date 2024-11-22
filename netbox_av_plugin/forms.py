from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from dcim.models import Device, Interface, Region, Site, SiteGroup

from .models import AVInterface


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
        fields = (
            "name",
            "enabled",
            "device",
            "videorate",
            "signaltype",
            "medium",
            "direction",
            "comments",
            "tags",
            )

class AVInterfaceFilterForm(NetBoxModelFilterSetForm):

    model = AVInterface
    videorate = forms.ModelMultipleChoiceField(
        queryset=AVInterface.objects.all(),
        required=False
    )