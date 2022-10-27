
from distutils.text_file import TextFile

from django import forms

from cacke.models import Bulka


class SearchForm(forms.Form):
    nachinka = forms.ModelChoiceField(Bulka.objects.order_by().values_list('nachinka',flat=True).distinct(), required=False)
    
    


