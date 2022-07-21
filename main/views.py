from django.shortcuts import render
from django.views import View
import requests
from woocommerce import API

# Create your views here.
class LinkActionView(View):
    template_name = "LinkActions_page.html"
    def get(self, request, *args, **kwargs):
        context = {}
        context['urltag'] = 'Nothing to display'
        return render(request, self.template_name, context)