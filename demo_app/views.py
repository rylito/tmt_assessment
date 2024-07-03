from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.

class TestView(TemplateView):
    template_name = 'demo_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['test_data'] = 'This is added context'

        return context
