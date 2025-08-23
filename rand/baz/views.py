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

