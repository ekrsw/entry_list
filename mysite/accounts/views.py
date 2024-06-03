from django.shortcuts import render
from django.views.generic import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)
