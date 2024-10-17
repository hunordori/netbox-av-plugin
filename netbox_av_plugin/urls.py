from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("avs/", views.AVListView.as_view(), name="av_list"),
    path("avs/add/", views.AVEditView.as_view(), name="av_add"),
    path("avs/<int:pk>/", views.AVView.as_view(), name="av"),
    path("avs/<int:pk>/edit/", views.AVEditView.as_view(), name="av_edit"),
    path("avs/<int:pk>/delete/", views.AVDeleteView.as_view(), name="av_delete"),
    path(
        "avs/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="av_changelog",
        kwargs={"model": models.AV},
    ),
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
