from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import ClearableFileInput
from .models import News, Emails


class NewsCreateForm(forms.ModelForm):
    title = forms.CharField(label=_('Tytuł'))
    content = forms.CharField(widget=forms.Textarea, label=_('Treść'))
    image = forms.ImageField(label=_("Zdjęcie"), widget=ClearableFileInput, required=False)

    class Meta:
        model = News
        fields = ['title', 'content', 'image']


class SendEmailForm(forms.ModelForm):
    name = forms.CharField(label=_('Imię i nazwisko'))
    email = forms.EmailField(label=_('Email'), max_length=100)
    title = forms.CharField(label=_('Temat'))
    content = forms.CharField(widget=forms.Textarea, label=_('Wiadomość'))

    class Meta:
        model = Emails
        fields = ['name', 'email', 'title', 'content']
