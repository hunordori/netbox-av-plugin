from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import AV, AVInterface


class AVForm(NetBoxModelForm):
    class Meta:
        model = AV
        fields = ("name", "tags")

class AVInterfaceForm(NetBoxModelForm):
    class Meta:
        model = AVInterface
        comments = CommentField()
        fields = ("name", "enabled", "device", "videorate", "medium", "direction", "comments", "tags")
