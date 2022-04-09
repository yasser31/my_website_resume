from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy

"""
def index(request):
    return render(request, "dashboard/index.html")
"""

class IndexView(FormView):
    template_name = 'dashboard/index.html'
    form_class = ContactForm
    success_url = reverse_lazy('dashboard:success')

    def form_valid(self, form):
        form.send()
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = 'dashboard/success.html'
