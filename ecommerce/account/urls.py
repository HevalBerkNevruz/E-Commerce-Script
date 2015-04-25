from django.conf.urls import url, include

from django.contrib import admin
from django.views.generic import TemplateView
from ecommerce.account.views import AccountInformationView

urlpatterns = [
    url(r'^siparis/', TemplateView.as_view(template_name='account/account-order.html')),
    url(r'^uyelik-bilgileri/', AccountInformationView.account_information),
    url(r'^adres-bilgileri/', TemplateView.as_view(template_name='account/account-address.html')),
    url(r'^adres-ekle/', TemplateView.as_view(template_name='account/account-address-add.html')),
    url(r'^hosgeldiniz/', TemplateView.as_view(template_name='entry.html')),
]
