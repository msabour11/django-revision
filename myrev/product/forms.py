from product.models import Product ,Category
from django import forms

class ProductForm(forms.Form):

    title = forms.CharField(required=True)
    price=forms.IntegerField()
    description = forms.CharField()
    category=forms.ModelChoiceField(Category.objects.all(),label='category')
    image = forms.ImageField()



class ProductFormModel(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
