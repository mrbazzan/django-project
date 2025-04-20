from django.contrib import admin

from .models import Comment, Test
from .forms import TestAdminForm


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    form = TestAdminForm
    # fields = ("image",)
    # readonly_fields = ('image',)


admin.site.register(Comment)
