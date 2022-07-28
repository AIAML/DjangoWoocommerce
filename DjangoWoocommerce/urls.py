"""DjangoWoocommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import LinkActionView,ReadAllProductsView,ReadAllProductsAttributesView,ReadAllCategoriesView,ReadAllTagsView,ReadAllReviewView\
    ,RetrieveSalesReportView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LinkActionView.as_view(),name='home'),
    path('ReadAllProducts/', ReadAllProductsView.as_view(),name='ReadAllProducts'),
    path('ReadAllProductsAttributes/', ReadAllProductsAttributesView.as_view(),name='ReadAllProductsAttributes'),
    path('ReadAllCategories/', ReadAllCategoriesView.as_view(),name='ReadAllCategories'),
    path('ReadAllCategories/', ReadAllCategoriesView.as_view(),name='ReadAllCategories'),
    path('ReadAllTags/', ReadAllTagsView.as_view(),name='ReadAllTags'),
    path('ReadAllReview/', ReadAllReviewView.as_view(),name='ReadAllReview'),
    path('RetrieveSalesReport/', RetrieveSalesReportView.as_view(),name='RetrieveSalesReport'),



    url(r'^Home/$', LinkActionView.as_view(), name='home'),
    url(r'^ReadAllProducts/$', ReadAllProductsView.as_view(), name='ReadAllProducts'),
    url(r'^ReadAllProductsAttributes/$', ReadAllProductsAttributesView.as_view(), name='ReadAllProductsAttributes'),
    url(r'^ReadAllCategories/$', ReadAllCategoriesView.as_view(), name='ReadAllCategories'),
    url(r'^ReadAllTags/$', ReadAllTagsView.as_view(), name='ReadAllTags'),
    url(r'^ReadAllReview/$', ReadAllReviewView.as_view(), name='ReadAllReview'),
    url(r'^RetrieveSalesReport/$', RetrieveSalesReportView.as_view(), name='RetrieveSalesReport'),

]
