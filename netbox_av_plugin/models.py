from django.db import models
from django.urls import reverse
from django.apps import apps
from django.contrib.postgres.fields import ArrayField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from netbox.models import NetBoxModel
from netbox.choices import ColorChoices

from dcim.choices import *
from dcim.constants import *
from dcim.models import Device, DeviceRole

from utilities.fields import ColorField, NaturalOrderingField
from utilities.ordering import naturalize_interface
from utilities.choices import ChoiceSet
from utilities.tracking import TrackingModelMixin

class AV(NetBoxModel):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_av_plugin:av", args=[self.pk])

class MediumChoices(ChoiceSet):
    CHOICES = [
        ('SDI', 'SDI'),
        ('HDMI', 'HDMI'),
        ('VGA', 'VGA'),
        ('DVI', 'DVI'),
        ('DP', 'Display Port'),
        ('XLR3', 'XLR 3-pin'),
        ('XLR4', 'XLR 4-pin'),
        ('BNC', 'BNC'),
    ]
class VideoSignalRateChoices(ChoiceSet):
    CHOICES = [
        ('SDI15GLVLA', 'SDI 1.5G Level A'),
        ('SDI3GLVLA', 'SDI 3G Level A'),
        ('SDI6GLVLA', 'SDI 6G Level A'),
        ('SDI12GLVLA', 'SDI 12G Level A'),
        ('SDI15GLVLB', 'SDI 1.5G Level B'),
        ('SDI3GLVLB', 'SDI 3G Level B'),
        ('SDI6GLVLB', 'SDI 6G Level B'),
        ('SDI12GLVLB', 'SDI 12G Level B'),
        ('HDMI12', 'HDMI 1.2'),
        ('HDMI14', 'HDMI 1.4'),
        ('HDMI20', 'HDMI 2.0'),
        ('DP12', 'Display Port 1.2'),
        ('DP14', 'Display Port 1.4'),
        ('DP2', 'Display Port 2.0'),
        ('RCA', 'RCA'),
        ('COAX', 'Coax'),
    ]

class SignalTypeChoices(ChoiceSet):
    CHOICES = [
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('video_audio', 'Video and Audio'),
        ('genlock', 'Genlock'),
        ('timecode', 'Timecode'),
        ('data', 'Data'),
    ]

class SignalDirectionChoices(ChoiceSet):
    CHOICES = [
        ('input', 'Input'),
        ('output', 'Output'),
        ('configurable', 'Configurable'),
    ]


class AVInterface(NetBoxModel, TrackingModelMixin):
    """
    A network interface within a Device. A physical Interface can connect to exactly one other Interface.
    """
    name = models.CharField(max_length=100)

    device = models.ForeignKey(
        'dcim.Device',
        on_delete=models.PROTECT,
        related_name='av_interfaces',
        blank=True,
        null=True,
    )

    enabled = models.BooleanField(
        verbose_name=('enabled'),
        default=True
    )

    label = models.CharField(
        verbose_name=('label'),
        max_length=60,
        blank=True,
        help_text=('Physical label')
    )

    videorate = models.CharField(
        verbose_name=('videorate'),
        max_length=50,
        choices=VideoSignalRateChoices,
        blank=True,
        help_text=('Video Signal Rate'),
    )

    medium = models.CharField(
        verbose_name=('medium'),
        max_length=50,
        choices=MediumChoices,
        blank=True,
        help_text=('Connector medium like SDI, HDMI...')
        )
    
    direction = models.CharField(
        verbose_name=('direction'),
        choices=SignalDirectionChoices,
        blank=True,
        help_text=('Signal Direction'),
    )

    comments = models.TextField(blank=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "AV Interface"
        verbose_name_plural = "AV Interfaces"

    # Override ComponentModel._name to specify naturalize_interface function
    _name = NaturalOrderingField(
        target_field='name',
        naturalize_function=naturalize_interface,
        max_length=100,
        blank=True
    )

    clone_fields = ('device','videorate', 'medium')

    @classmethod
    def get_prerequisite_models(cls):
        return [apps.get_model("dcim.Device"), Device]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_av_plugin:avinterface", args=[self.pk])
