from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from ..models import AV, AVInterface

class AVInterfaceSerializer(NetBoxModelSerializer):

    class Meta:
        model = AVInterface
        url = serializers.HyperlinkedIdentityField(
            view_name='plugins-api:netbox_av_plugin-api:avinterface-detail'
        )
        fields = (
            'id', 'display', 'name', 'enabled', 'device', 'videorate', 'signaltype', 'medium', 'direction', 'comments', 'tags', 'created',
            'last_updated'
        )
        