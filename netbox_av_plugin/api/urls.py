from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_av_plugin'

router = NetBoxRouter()
router.register('avinterface', views.AVInterfaceViewSet)

urlpatterns = router.urls