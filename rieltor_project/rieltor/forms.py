from django import forms
from  .models import Client, Review,Property


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client  # Связываем форму с моделью Client
        fields = ['name', 'surname', 'phone', 'email', 'description']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'rating', 'comment']


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['adress','city','price','floor']

class PropertySearchForm(forms.Form):
    city = forms.CharField(max_length=100, required=False, label='Город')
    price_max = forms.IntegerField(required=False, label='Максимальная цена')