from django.contrib.contenttypes.models import ContentType
from django.forms.widgets import Widget
from .models import Test
from django import forms


class RatingWidget(Widget):
    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        stars = "<span class=''>*</span>" * 5
        return f"<div class='rating'>{stars}</div>"


class TestAdminForm(forms.ModelForm):
    # ratings = forms.IntegerField(
    #     widget=RatingWidget(attrs={'class': 'custom-rating'})
    # )

    class Meta:
        model = Test
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     print(self.fields)
    #     self.fields['content_type'].queryset = ContentType.objects.filter(id=45)
