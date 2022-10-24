
from distutils.text_file import TextFile
from django import forms


class SearchForm(forms.Form):
    search_string = forms.CharField(max_length=100, required=False)
