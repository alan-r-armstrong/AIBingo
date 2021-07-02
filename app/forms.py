from enum import auto
from django import forms
from datetime import datetime
from PIL import Image
from django.forms.widgets import Widget
from django.utils.formats import FORMAT_SETTINGS

class CharacterForm(forms.Form):
    name = forms.CharField(max_length=15)
    affiliation = forms.CharField(max_length=15)
    char_pic = forms.ImageField ()
    char_desc = forms.CharField (widget=forms.Textarea, max_length=255)
    char_quotes = forms.CharField (max_length=5000)