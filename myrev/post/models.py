from django.db import models
from django.shortcuts import render,redirect,reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=3000)
    image = models.ImageField(upload_to='media/images', blank=True,null=True)
    # updated = models.DateTimeField(auto_now_add=True)
    # created=models.DateTimeField(auto_created=True)



    def __str__(self):
       return f'{self.title}'
    

    def get_image_url(self):
        return f'/media/{self.image}'
    
    def get_edit_url(self):
        return reverse('post.edit', args=[self.id])
    


    def get_delete_url(self):
        return reverse('post.delete', args=[self.id])
    

    def get_show_url(self):
        return reverse('post.show', args=[self.id])
    
    @classmethod
    def get_index_url(cls):
        return reverse('post.list')