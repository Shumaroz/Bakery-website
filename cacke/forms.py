
from distutils.text_file import TextFile
from email.policy import default

from django import forms
from django.conf import settings
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from cacke.models import Bulka


class SearchForm(forms.Form):
    nachinka = forms.ModelChoiceField(Bulka.objects.order_by().values_list('nachinka',flat=True).distinct(), required=False, label="Начинка")
    testo = forms.ModelChoiceField(Bulka.objects.order_by().values_list('testo',flat=True).distinct(), required=False, label="Тесто")
    price_l = forms.IntegerField(required=False)
    price_r = forms.IntegerField(required=False)
    name = forms.CharField(required=False, label="Название")

    def get_price(self):
        dat = [self.data['price_l'],self.data['price_r']]
                    
        return dat

    def get_nach(self):
        nach = self.data['nachinka']
        return nach
    
    def get_test(self):
        test = self.data['testo']
        return test

    def get_name(self):
        name = self.data['name']
        return name


