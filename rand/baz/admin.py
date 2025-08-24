from django.contrib import admin

from cms.admin.placeholderadmin import FrontendEditableAdminMixin
from .models import Relationship, Spouse, Comment, Test
from .forms import TestAdminForm


@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    pass


@admin.register(Spouse)
class SpouseAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
    frontend_editable_fields = ("name",)


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    form = TestAdminForm
    # fields = ("image",)
    # readonly_fields = ('image',)


admin.site.register(Comment)
