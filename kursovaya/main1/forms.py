from django import forms
from .models import Carrier


class CarrierForm(forms.ModelForm):
    class Meta:
        model = Carrier
        fields = ( 'itinerary', 'date', 'firm', 'customers_contact_person', 'auto', 'note')
