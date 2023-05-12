from django import forms
from django.contrib.auth.models import *
from .models import *

class position(forms.Form):
    latitude = forms.FloatField(required=False, widget=forms.HiddenInput(
        attrs={'id': 'lat', 'name': 'lat'}))
    longitude = forms.FloatField(required=False, widget=forms.HiddenInput(
        attrs={'id': 'lng', 'name': 'lng'}))

    def is_valid(self):
        lat = self.data['latitude']
        lng = self.data['longitude']
        if lat == '' or lng == '':
            self.add_error("latitude", "choisit votre position")
        value = super(position, self).is_valid()
        return value

  