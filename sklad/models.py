from django.db import models
from django.contrib.auth.models import User


# class User(models.Model):
#     name = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user')
#     position = models.CharField(max_length=55, verbose_name='должность')
    
#     def __str__(self):
#         return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=55)
    descriction = models.TextField()
    url = models.URLField(verbose_name='ссылка')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'категории'
    
    
class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user')
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='category') 
    name = models.CharField(max_length=55, verbose_name='наименование товара')
    amount = models.IntegerField(verbose_name='количество')
    price = models.IntegerField(verbose_name='цена')
    madein = models.CharField(max_length=55, verbose_name='производство')
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'продукты'
    


    
    
    
    
    
    
    
    
