from django import forms
from app1.models import StateModel,CityModel,CuisineModel

class StateForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = StateModel

class CityForm(forms.ModelForm):
    city_state = forms.ModelMultipleChoiceField(queryset=StateModel.objects.only('name'))
    class Meta:
        fields = '__all__'
        model = CityModel



class CuisineForm(forms.ModelForm):
    ty=(('Bakery','Bakery'),('Beverages','Beverages'),('Restaurants','Restaurants'))
    type = forms.ChoiceField(choices=ty)
    class Meta:
        fields = '__all__'
        model = CuisineModel

