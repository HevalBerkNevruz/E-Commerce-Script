from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from ecommerce.account.forms import AccountInformationForm, AddressInformationForm
from ecommerce.account.models import Address
from ecommerce.user.models import User


class AccountInformationView(View):
    def account_information(request):
        if request.method == "POST":
            form = AccountInformationForm(request.POST)
            if form.is_valid():
                secure_data = form.cleaned_data
                User.objects.filter(id__exact=request.session["id"]).update(name=secure_data["name"],
                                                                            surname=secure_data["surname"],
                                                                            phone_number=secure_data["phone_number"],
                                                                            gender=secure_data["gender"],
                                                                            birthday=secure_data["birthday"])
                return render_to_response("account/account-information.html", {"form": form},
                                          context_instance=RequestContext(request))
            else:
                return render_to_response("account/account-information.html", {"form": form},
                                          context_instance=RequestContext(request))
        else:
            user = User.objects.get(id=request.session["id"])
            form = AccountInformationForm(
                initial={"email": user.email, "name": user.name, "surname": user.surname,
                         "phone_number": user.phone_number, "gender": user.gender, "birthday": user.birthday})
            return render_to_response("account/account-information.html", {"form": form, "user": user},
                                      context_instance=RequestContext(request))


class AddressInformationView(View):
    def account_address_select(request):
        address = Address.objects.get(user_id__exact=request.session["id"])
        id = address.id
        return render_to_response("account/account-address.html", {"address": address, "id": id},
                                  context_instance=RequestContext(request))

    def account_address_add(request):
        if request.method == "POST":
            form = AddressInformationForm(request.POST)
            if form.is_valid():
                secure_data = form.cleaned_data
                address = Address(user_id=request.session["id"], address_header=secure_data["address_header"],
                                  name_surname=secure_data["name_surname"], city=secure_data["city"],
                                  county=secure_data["county"], post_code=secure_data["post_code"],
                                  address=secure_data["address"],
                                  cell_phone=secure_data["cell_phone"], phone=secure_data["phone"],
                                  identification_number=secure_data["identification_number"])
                address.save()
                return HttpResponseRedirect("/adres-bilgileri/")
            else:
                return render_to_response("account/account-address-add.html", {"form": form},
                                          context_instance=RequestContext(request))
        else:
            form = AddressInformationForm()
            return render_to_response("account/account-address-add.html", {"form": form},
                                      context_instance=RequestContext(request))

