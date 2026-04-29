
from django import forms

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import GistPluginModel
from .widgets import Select2TagWidget


class GistPluginForm(forms.ModelForm):
    class Meta:
        model = GistPluginModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        qs = (
            GistPluginModel.objects
            .exclude(gist_user="")
            .values_list("gist_user", flat=True)
            .distinct()
            .order_by("gist_user")
        )
        choices = [("", "")] + [(item, item) for item in qs]

        self.fields["gist_user"].widget = Select2TagWidget(
            choices=choices,
            select2_options={"placeholder": "Type something..."},
        )


class GistPlugin(CMSPluginBase):
    name = "Gist"
    form = GistPluginForm
    model = GistPluginModel
    render_template = "gist/_gist_plugin.html"  # partial template
    text_enabled = True


plugin_pool.register_plugin(GistPlugin)
