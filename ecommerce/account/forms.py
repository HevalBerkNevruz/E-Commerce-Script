from django import forms


class AccountInformationForm(forms.Form):
    CHOICES = [('1', 'Erkek'), ('2', 'Bayan')]
    email = forms.CharField(label="Email", max_length=100, widget=forms.TextInput(attrs={"readonly": "readonly"}))
    name = forms.CharField(label="Ad", max_length=100)
    surname = forms.CharField(label="Soyad", max_length=100)
    phone_number = forms.CharField(label="Telefon", max_length=100)
    gender = forms.ChoiceField(label="Cinsiyet", required=False, choices=CHOICES, widget=forms.RadioSelect())
    birthday = forms.DateField(label="Doğum Tarihi", required=False)


class AddressInformationForm(forms.Form):
    address_header = forms.CharField(label="Adres Başlığı", max_length=100)
    name_surname = forms.CharField(label="Ad Soyad", max_length=150)
    city = forms.CharField(label="İl", max_length=100)
    county = forms.CharField(label="İlçe", max_length=100)
    post_code = forms.CharField(label="Posta Kodu", max_length=5)
    address = forms.CharField(label="Adres",widget=forms.Textarea(attrs={'class':'form-control'}))
    cell_phone = forms.CharField(label="Cep Telefonu", max_length=11)
    phone = forms.CharField(label="Ev Telefonu", required=False, max_length=11)
    identification_number = forms.CharField(label="TC Kimlik No", max_length=100)
