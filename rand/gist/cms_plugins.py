
from django import forms

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from easy_select2.widgets import Select2

from .models import GistPluginModel


class GistPluginForm(forms.ModelForm, forms.TextInput):
    class Meta:
        model = GistPluginModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(GistPluginForm, self).__init__(*args, **kwargs)

        def get_choices():
            qs = GistPluginModel.objects.values_list(
                "gist_user", flat=True
            ).distinct().order_by("gist_user")
            return [(item, str(item)) for item in qs]

        self.fields["gist_user"].widget = Select2(
            choices = get_choices(),
            select2attrs = {
                "tags": "true",
                "placeholder": "Type something...",
                "tokenSeparators": [';', '\n' ],
                "width": "100%",
            }
        )


class GistPlugin(CMSPluginBase):
    name = "Gist"
    form = GistPluginForm
    model = GistPluginModel
    render_template = "gist/_gist_plugin.html"  # partial template
    text_enabled = True


plugin_pool.register_plugin(GistPlugin)
