from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import EntryModel


def hello_world(request):
    return HttpResponse("Hello, world. You're at the entryapp index.")

class ListEntryView(ListView):
    template_name = 'entry/entrymodel_list.html'
    model = EntryModel

class DetailEntryView(DetailView):
    template_name = 'entry/entry_detail.html'
    model = EntryModel