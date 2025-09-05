from django.shortcuts import render
from django.shortcuts import reverse
from django.views.generic import DetailView, ListView

from .models import Spouse

# Create your views here.

class SpouseListView(ListView):
    model = Spouse
    queryset = Spouse.objects.all()

    def render_to_response(self, context, **kwargs):
        if self.request.toolbar:
            menu = self.request.toolbar.get_or_create_menu("staff-menu", "Staff")  # staff-list-menu
            menu.add_sideframe_item("Relationship List", url=reverse("admin:baz_relationship_changelist"))
            menu.add_modal_item("Add new relationship member", url=reverse("admin:baz_relationship_add"))
            menu.add_break()
            menu.add_sideframe_item("Staff List", url=reverse("admin:baz_spouse_changelist"))
            menu.add_modal_item("Add new staff member", url=reverse("admin:baz_spouse_add"))

        return super().render_to_response(context, **kwargs)


class SpouseDetailView(DetailView):
    model = Spouse
    context_object_name = "spouse"

    def render_to_response(self, context, **kwargs):
        if self.request.toolbar and self.request.toolbar.edit_mode_active:
            menu = self.request.toolbar.get_or_create_menu("staff-member-menu", self.object.name)
            menu.add_modal_item(
                f"Edit {self.object.name}",
                url=reverse("admin:baz_spouse_change", kwargs={"object_id": self.object.id}))

        return super().render_to_response(context, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.toolbar.set_object(self.object)
        return context


# cms edit endpoint requires this signature
def spouse_detail_view(request, obj):
    return SpouseDetailView.as_view()(request, pk=obj.pk)

