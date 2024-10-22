from django.conf import settings
from netbox.plugins import PluginMenu, PluginMenuButton, PluginMenuItem

plugin_settings = settings.PLUGINS_CONFIG["netbox_av_plugin"]


menu_buttons = (
    PluginMenuItem(
        link="plugins:netbox_av_plugin:avinterface_list",
        link_text="AV Interface List",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_av_plugin:avinterface_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
            ),
        ),
    ),
)

if plugin_settings.get("top_level_menu"):
    menu = PluginMenu(
        label="Audio Video",
        groups=(("Interfaces", menu_buttons),),
        icon_class="mdi mdi-video",
    )
else:
    menu_items = menu_buttons