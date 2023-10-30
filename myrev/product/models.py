from django.db import models
from django.shortcuts import reverse,redirect
from django.utils.translation import gettext as _

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('categorie')


    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255,null=True)
    price=models.IntegerField(default=12, null=True)
    description = models.TextField(blank=True, max_length=255,null=True)
    category=models.ForeignKey(Category, null=True,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/images',null=True)



    def __str__(self):
        return self.title
    

    def get_image_url(self):
        return f'/media/{self.image}'
    
    def get_detial_url(self):
        url=reverse('product.detail', args=[self.id])
        return url
    
    def get_delete_url(self):
        url=reverse('product.delete', args=[self.id])
        return url
    
    def get_edit_url(self):
        url=reverse('product.edit', args=[self.id])
        return url
    
    # def  get_home_url(self):
    #     url=('product.index') 
    #     return redirect(url)
    
    # def get_all_products(self):
    #     return self.objects.all()
    @classmethod
    def get_speacified_product(cls,id):
        return cls.objects.get(id=id)

