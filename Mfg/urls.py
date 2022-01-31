"""Mfg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from operator import imod
from os import stat
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mfgadmin import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',views.api),
    path('promotion/',views.promotions,name="promotion"),
    path('promo/',views.promotion,name="promo"),
    path('assign-promo/',views.assign_promo,name="assign_promo"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
