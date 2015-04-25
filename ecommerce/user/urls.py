from django.conf.urls import url, include

from django.contrib import admin

from ecommerce.user.views import SignUpView, SignInView


urlpatterns = [
    url(r'^uye-ol/', SignUpView.sign_up),
    url(r'^giris/', SignInView.sign_in),
    url(r'^cikis/', SignInView.sign_out),
]
