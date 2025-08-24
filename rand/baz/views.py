from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Spouse

# Create your views here.

class SpouseListView(ListView):
    model = Spouse
    queryset = Spouse.objects.all()

class SpouseDetailView(DetailView):
    model = Spouse
    context_object_name = "spouse"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.toolbar.set_object(self.object)
        return context


# cms edit endpoint requires this signature
def spouse_detail_view(request, obj):
    return SpouseDetailView.as_view()(request, pk=obj.pk)

