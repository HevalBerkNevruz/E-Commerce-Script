from django import forms
from ecommerce.user.models import User


class SignUpForm(forms.Form):
    CHOICES = [('1', 'Erkek'), ('2', 'Bayan')]
    name = forms.CharField(max_length=50, label="Ad")
    surname = forms.CharField(max_length=50, label="Soyad")
    email = forms.EmailField(max_length=100, label="Email")
    password = forms.CharField(min_length=6, max_length=16, label="Şifre", widget=forms.PasswordInput)
    re_password = forms.CharField(min_length=6, max_length=16, label="Şifre Tekrarı", widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=11, label="Telefon Numarası")
    gender = forms.ChoiceField(required=False, label="Cinsiyet", choices=CHOICES, widget=forms.RadioSelect())
    birthday = forms.DateField(required=False, label="Doğum Tarihi")

    """def clean_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if password != re_password:
            raise forms.ValidationError("Şifreler eşleşmiyor")
        return self.cleaned_data
"""
    def clean_email_already(self):
        try:
            email = self.cleaned_data.get("email")
            if User.objects.filter(email__exact=email).exists():
                raise forms.ValidationError("Mail adresi ile daha önce kayıt olunmuş")
            return self.email
        except:
            return ""

    def clean(self):
        self.clean_email_already()
        return super(SignUpForm, self).clean()


class SignInForm(forms.Form):
    email = forms.EmailField(max_length=100, label="Email")
    password = forms.CharField(min_length=6, max_length=16, label="Şifre", widget=forms.PasswordInput)