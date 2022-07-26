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

class ReadAllProductsView(View):
    template_name = "ReadAllProducts_page.html"
    def get(self, request, *args, **kwargs):
        context = {}
        context['urltag'] = 'Nothing to display'
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            passed_data = request.POST
            urltext = request.POST.get('urltext')
            Consumer_Key = request.POST['Consumer_Key']
            Consumer_Secret = request.POST['Consumer_Secret']
        url = urltext

        wcapi = API(
            url=urltext,
            consumer_key=Consumer_Key,
            consumer_secret=Consumer_Secret,
            timeout=50
        )
        context['urltag'] = wcapi.get("products").json()
        return render(request, self.template_name, context)

class ReadAllProductsAttributesView(View):
        template_name = "ReadAllProductsAttributes_page.html"

        def get(self, request, *args, **kwargs):
            context = {}
            context['urltag'] = 'Nothing to display'
            return render(request, self.template_name, context)

        def post(self, request, *args, **kwargs):
            context = {}
            if request.method == 'POST':
                passed_data = request.POST
                urltext = request.POST.get('urltext')
                Consumer_Key = request.POST['Consumer_Key']
                Consumer_Secret = request.POST['Consumer_Secret']
            url = urltext

            wcapi = API(
                url=urltext,
                consumer_key=Consumer_Key,
                consumer_secret=Consumer_Secret,
                timeout=50
            )
            context['urltag'] = wcapi.get("products/attributes").json()
            return render(request, self.template_name, context)


class ReadAllCategoriesView(View):
    template_name = "ReadAllCategories_page.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context['urltag'] = 'Nothing to display'
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            passed_data = request.POST
            urltext = request.POST.get('urltext')
            Consumer_Key = request.POST['Consumer_Key']
            Consumer_Secret = request.POST['Consumer_Secret']
        url = urltext

        wcapi = API(
            url=urltext,
            consumer_key=Consumer_Key,
            consumer_secret=Consumer_Secret,
            timeout=50
        )
        context['urltag'] = wcapi.get("products/categories").json()
        return render(request, self.template_name, context)

class ReadAllTagsView(View):
    template_name = "ReadAllTags_page.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context['urltag'] = 'Nothing to display'
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            passed_data = request.POST
            urltext = request.POST.get('urltext')
            Consumer_Key = request.POST['Consumer_Key']
            Consumer_Secret = request.POST['Consumer_Secret']
        url = urltext

        wcapi = API(
            url=urltext,
            consumer_key=Consumer_Key,
            consumer_secret=Consumer_Secret,
            timeout=50
        )
        context['urltag'] = wcapi.get("products/tags").json()
        return render(request, self.template_name, context)