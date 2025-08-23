from django.contrib import admin

from .models import Relationship, Spouse, Comment, Test
from .forms import TestAdminForm


@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    pass


@admin.register(Spouse)
class SpouseAdmin(admin.ModelAdmin):
    pass


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    form = TestAdminForm
    # fields = ("image",)
    # readonly_fields = ('image',)


admin.site.register(Comment)
