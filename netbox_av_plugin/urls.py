from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("avinterfaces/", views.AVInterfaceListView.as_view(), name="avinterface_list"),
    path("avinterfaces/add/", views.AVInterfaceEditView.as_view(), name="avinterface_add"),
    path("avinterfaces/<int:pk>/", views.AVInterfaceView.as_view(), name="avinterface"),
    path("avinterfaces/<int:pk>/edit/", views.AVInterfaceEditView.as_view(), name="avinterface_edit"),
    path("avinterfaces/<int:pk>/delete/", views.AVInterfaceDeleteView.as_view(), name="avinterface_delete"),
    path(
        "avinterfaces/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="avinterface_changelog",
        kwargs={"model": models.AVInterface},
    ),
)
