from django.db import models

# Create your models here.


from django.db import models


class Shirt(models.Model):
    Name = models.CharField(max_length=100)
    Size = models.CharField(max_length=2,default="M")
    StokeSize = models.IntegerField(default=0)
    Price = models.FloatField(default=0)
    Kind = models.CharField(max_length=10, default="Shirts")
    Image = models.ImageField( blank=True)


class Pant(models.Model):
    Name = models.CharField(max_length=100)
    Size = models.CharField(max_length=2, default="M")
    StokeSize = models.IntegerField(default=0)
    Price = models.FloatField(default=0)
    Kind = models.CharField(max_length=10, default="Pants")
    Image = models.ImageField(upload_to='uploads/pants/', max_length=45, blank=True)

class Jacket(models.Model):
    Name = models.CharField(max_length=100)
    Size = models.CharField(max_length=2, default="M")
    StokeSize = models.IntegerField(default=0)
    Price = models.FloatField(default=0)
    Kind = models.CharField(max_length=10, default="Jackets")
    Image = models.ImageField(upload_to='uploads/jackets/', max_length=45, blank=True)


class T_shirt(models.Model):
    Name = models.CharField(max_length=100)
    Size = models.CharField(max_length=2, default="M")
    StokeSize = models.IntegerField(default=0)
    Price = models.FloatField(default=0)
    Kind = models.CharField(max_length=10,default="T-Shirts")
    Image = models.ImageField(upload_to='uploads/t_shirts/', max_length=45, blank=True)

class Accessories(models.Model):
    Category = models.CharField(max_length=100)
    Kind = models.CharField(max_length=10,default="Accessories")
    Name = models.CharField(max_length=100)
    Size = models.CharField(max_length=2, default="M")
    StokeSize = models.IntegerField(default=0)
    Price = models.FloatField(default=0)
    Image = models.ImageField(upload_to='uploads/t_shirts/', max_length=45, blank=True)



class Slides(models.Model):
    Title = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='uploads/slides/', max_length=45, blank=False)
    Comments = models.CharField(max_length=200)
    Link = models.URLField(default="#")


