from django import forms

from events.models import Event

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ("slug","isActive")
        labels = {
            "name":"Etkinlik Adı:",
            "desc":"Açıklama:",
            "date":"Tarih:",
            "time":"Saat:",
            "eventDuration":"Etkinlik Süresi:",
            "location":"Konum:",
            "category":"Kategori:",
        }
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "date":forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "desc":forms.Textarea(attrs={"class":"form-control"}),
            "time":forms.TextInput(attrs={"class":"form-control"}),
            "eventDuration":forms.TextInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            "category":forms.TextInput(attrs={"class":"form-control"}),
        }

class EventEditForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ("slug","isActive")
        labels = {
            "name":"Etkinlik Adı:",
            "desc":"Açıklama:",
            "date":"Tarih:",
            "time":"Saat:",
            "eventDuration":"Etkinlik Süresi:",
            "location":"Konum:",
            "category":"Kategori:",
        }
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "date":forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "desc":forms.Textarea(attrs={"class":"form-control"}),
            "time":forms.TextInput(attrs={"class":"form-control"}),
            "eventDuration":forms.TextInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            "category":forms.TextInput(attrs={"class":"form-control"}),
        }