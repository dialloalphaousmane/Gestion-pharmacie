from django import forms
from django.forms import modelformset_factory
from .models import Produits, Vente, DetailVente


class AjoutProduit(forms.ModelForm):
    class Meta:
        model = Produits
        fields = [
            'name', 'category', 'price', 'quantite', 'description', 'date_expiration', 'image'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nom du produit', 'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Prix', 'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={'placeholder': 'Quantité', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'class': 'form-control', 'rows': 4}),
            'date_expiration': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }


class AjoutVenteForm(forms.ModelForm):
    customer = forms.CharField(
        help_text='Nom du client',
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nom du client', 'class': 'form-control'})
    )

    class Meta:
        model = Vente
        fields = ['customer']


# FormSet pour vendre plusieurs produits en même temps
DetailVenteFormSet = modelformset_factory(
    DetailVente,
    fields=('produit', 'quantite', 'prix_unitaire'),
    extra=3,
    widgets={
        'produit': forms.Select(attrs={'class': 'form-control'}),
        'quantite': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        'prix_unitaire': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
    }
)
