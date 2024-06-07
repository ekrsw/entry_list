from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import EntryModel


def hello_world(request):
    return HttpResponse("Hello, world. You're at the entryapp index.")

class ListEntryView(LoginRequiredMixin, ListView):
    template_name = 'entry/entrymodel_list.html'
    model = EntryModel

class DetailEntryView(LoginRequiredMixin, DetailView):
    template_name = 'entry/entry_detail.html'
    model = EntryModel

class CreateEntryView(LoginRequiredMixin, CreateView):
    template_name = 'entry/entry_create.html'
    model = EntryModel
    fields = ['title', 'entry_text']
    success_url = reverse_lazy('entryapp:entry_list')

    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.user = self.request.user
        entry.save()
        return super().form_valid(form)

class UserView(LoginRequiredMixin, ListView):
    template_name = 'entry/entrymodel_list.html'
    paginate_by = 9

    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = EntryModel.objects.filter(
            user=user_id
        )
        return user_list