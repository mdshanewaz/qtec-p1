from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    title = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Categories"


class BrandModel(models.Model):
    title = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Brands"


class WarrantyModel(models.Model):
    year = models.PositiveIntegerField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Warranties"
        ordering = ['year']


class ProductModle(models.Model):
    mainimage = models.ImageField(upload_to='Products')
    name = models.CharField(max_length=264)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='category')
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    warranty = models.ForeignKey(WarrantyModel, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Description')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.name
    
    class Meta:
        ordering = ['-created']
