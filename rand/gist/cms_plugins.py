
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import GistPluginModel


class GistPlugin(CMSPluginBase):
    name = "Gist"
    model = GistPluginModel
    render_template = "gist/_gist_plugin.html"  # partial template
    text_enabled = True


plugin_pool.register_plugin(GistPlugin)
