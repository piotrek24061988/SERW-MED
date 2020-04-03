from django import forms
from django.utils.translation import gettext_lazy as _
from .models import News


class NewsCreateForm(forms.ModelForm):
    title = forms.CharField(label=_('Tytuł'))
    content = forms.CharField(widget=forms.Textarea, label=_('Treść'))

    class Meta:
        model = News
        fields = ['title', 'content']
