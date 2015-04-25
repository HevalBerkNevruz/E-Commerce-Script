from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
import time

from ecommerce.user.forms import SignUpForm, SignInForm
from ecommerce.user.models import User


class SignUpView(View):
    def sign_up(request):
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                secure_data = form.cleaned_data
                user = User(
                    name=secure_data["name"],
                    surname=secure_data["surname"],
                    email=secure_data["email"],
                    password=secure_data["password"],
                    phone_number=secure_data["phone_number"],
                    gender=secure_data.get("gender"),
                    birthday=secure_data.get("birthday"),
                )
                user.save()
                return HttpResponseRedirect("/giris/")
            else:
                return render_to_response("sign-up.html", {"form": form}, context_instance=RequestContext(request))
        else:
            form = SignUpForm()
            return render_to_response("sign-up.html", {"form": form}, context_instance=RequestContext(request))


class SignInView(View):
    def sign_in(request):
        if request.method == "POST":
            form = SignInForm(request.POST)
            if form.is_valid():
                secure_data = form.cleaned_data
                user = User.objects.get(email__exact=secure_data["email"])
                if user.password == secure_data["password"]:
                    request.session["id"] = user.id
                    request.session["name"] = user.name
                    request.session["surname"] = user.surname
                    request.session["logged_in"] = True
                    return render_to_response("entry.html",
                                              {"name": user.name, "surname": user.surname},
                                              context_instance=RequestContext(request))
                else:
                    _class = "alert alert-danger"
                    message = "E-Mail adresi veya şifre yanlış"
                return render_to_response("sign-in.html", {"form": form, "class": _class, "message": message},
                                          context_instance=RequestContext(request))
            else:
                return render_to_response("sign-in.html", {"form": form}, context_instance=RequestContext(request))
        else:
            form = SignInForm()
            return render_to_response("sign-in.html", {"form": form}, context_instance=RequestContext(request))

    def sign_out(self):
        if "logged_in" in self.session:
            del self.session["id"]
            del self.session["name"]
            del self.session["surname"]
            del self.session["logged_in"]
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/")
