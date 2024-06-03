from django.forms import ModelForm
from django import forms
from .models import *


class MessageForm(ModelForm):
    class Meta:
        model = ChatMessages
        fields = ['body']
        widgets = {
            'body': forms.TextInput(
                attrs={'placeholder': 'Add Message....', 'class': 'p-4 text-black', "maxlength": '300',
                       'autofocus': True}),
        }
