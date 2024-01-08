from django.contrib import admin
from ProductApp.models import CategoryModel, BrandModel, WarrantyModel, ProductModle


# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(BrandModel)
admin.site.register(WarrantyModel)
admin.site.register(ProductModle)