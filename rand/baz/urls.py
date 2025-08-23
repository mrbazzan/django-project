
from django.urls import re_path
from .views import SpouseListView, SpouseDetailView
urlpatterns = [
    re_path(r"^$", SpouseListView.as_view(), name="spouselist"),
    re_path(r"^(?P<pk>[^/]+)/$", SpouseDetailView.as_view(), name="spousedetail"),
]
