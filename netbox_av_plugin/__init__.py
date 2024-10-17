"""Top-level package for NetBox AV Plugin."""

__author__ = """Hunor Dori"""
__email__ = "hello@hunor.xyz"
__version__ = "0.1.0"


from netbox.plugins import PluginConfig


class AVConfig(PluginConfig):
    name = "netbox_av_plugin"
    verbose_name = "NetBox AV Plugin"
    description = "Netbox Plugin for Audio Video interfaces"
    version = "version"
    base_url = "netbox_av_plugin"


config = AVConfig
