from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.forms import widgets
from .models import CustomUser
from django import forms


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})

class NewUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = {"username","email","first_name","last_name"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["last_name"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password1"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["password2"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control"})
        self.fields["email"].required = True
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True

    def clean_email(self):
        email = self.cleaned_data.get("email")
        
        if CustomUser.objects.filter(email = email).exists():
            self.add_error("email","Email daha önce kullanılmış")
        return email

class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["new_password2"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["old_password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})

class UploadForm(forms.Form):
    image = forms.ImageField()

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = {"username","first_name","last_name","image","email","location","phone_number","date_of_birth","gender","interests"}
        labels = {
            "username":"Kullanıcı Adı:",
            "first_name":"Adı:",
            "last_name":"Soyadı:",
            "image":"Profil Fotoğrafı",
            "email":"Email:",
            "location":"Konum:",
            "phone_number":"Telefon Numarası:",
            "date_of_birth":"Doğum Tarihi:",
            "gender":"Cinsiyet:",
            "interests":"İlgi Alanları:"
        }
        widgets = {
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            "phone_number":forms.TextInput(attrs={"class":"form-control"}),
            "date_of_birth":forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "gender":forms.Select(attrs={"class": "form-select"}, choices=[("E", "Erkek"), ("K", "Kadın")]),
            "interests":forms.Textarea(attrs={"class":"form-control"}),
        }