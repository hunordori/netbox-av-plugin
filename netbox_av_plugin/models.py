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

from .choices import *

class AV(NetBoxModel):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_av_plugin:av", args=[self.pk])


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

    signaltype = models.CharField(
        verbose_name=('signaltype'),
        max_length=50,
        choices=SignalTypeChoices,
        blank=True,
        help_text=('Signal type like video, audio, data')
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
