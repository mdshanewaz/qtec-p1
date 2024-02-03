from django import forms
from ProductApp.models import ProductModle, CategoryModel, BrandModel, WarrantyModel

# Forms Stat here

class ProductSearchForm(forms.Form):
    category = forms.ModelChoiceField(queryset=CategoryModel.objects.all(), empty_label="All Categories", required=False)
    brand = forms.ModelChoiceField(queryset=BrandModel.objects.all(), empty_label="All Brands", required=False)
    warranty = forms.ModelChoiceField(queryset=WarrantyModel.objects.all(), empty_label="All Warranties", required=False)
    min_price = forms.IntegerField(label='Min Price', required=False)
    max_price = forms.IntegerField(label='Max Price', required=False)
