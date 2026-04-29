import json

from django import forms


class Select2TagWidget(forms.Select):
    """A ``<select>`` widget rendered with Django admin's bundled select2.

    Behaves like a regular ``forms.Select`` but lets users either pick one of
    the provided choices or type a new value (select2 ``tags: true``).
    """

    def __init__(self, attrs=None, choices=(), select2_options=None):
        self.select2_options = {
            "tags": True,
            "tokenSeparators": [";", "\n"],
            "width": "100%",
            **(select2_options or {}),
        }
        super().__init__(attrs, choices)

    def build_attrs(self, base_attrs, extra_attrs=None):
        attrs = super().build_attrs(base_attrs, extra_attrs)
        css_class = (attrs.get("class", "") + " admin-select2-tag").strip()
        attrs["class"] = css_class
        attrs["data-select2-options"] = json.dumps(self.select2_options)
        return attrs

    @property
    def media(self):
        return forms.Media(
            css={"screen": ("admin/css/vendor/select2/select2.min.css",)},
            js=(
                "admin/js/vendor/jquery/jquery.min.js",
                "admin/js/vendor/select2/select2.full.min.js",
                "admin/js/jquery.init.js",
                "gist/js/select2_tag.js",
            ),
        )
