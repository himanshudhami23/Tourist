from datetime import date
from django.db import models
from django.db.models.fields import URLField
from django.utils.timezone import datetime
from django.contrib.auth import settings
# Create your models here.
class Category(models.Model):
    objects = models.Manager

    name = models.CharField(max_length=200)
    url = models.SlugField(editable=False,null=True,blank=True)

      # default Column

    is_active = models.BooleanField(default=True,editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )
    created_on = models.DateField(
        default=datetime.now, editable=False, null=True, blank=True
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name



class Movies(models.Model):
    objects = models.Manager

    category = models.ForeignKey(Category,on_delete=models.CASCADE,limit_choices_to={'is_active':True})
    name = models.CharField(max_length=200)    
    url = models.SlugField(editable=False,null=True,blank=True)
    image = models.ImageField(upload_to='movies/')
    taller_video = URLField(null=True,blank=True)
    language = models.CharField(max_length=50,null=True,blank=True)
    relished_date = models.DateField(default=datetime.now)
    producer_name = models.CharField(max_length=100)
    director_name = models.CharField(max_length=100)
    actress_name = models.TextField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)

      # default Column

    is_active = models.BooleanField(default=True,editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )
    created_on = models.DateField(
        default=datetime.now, editable=False, null=True, blank=True
    )

    class Meta:
        verbose_name = "Movies"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.name

class Actress_Images(models.Model):
    objects = models.Manager

    movie = models.ForeignKey(Movies,on_delete=models.CASCADE,limit_choices_to={'is_active':True})
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movies/actress/')

    # default Column

    is_active = models.BooleanField(default=True,editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )
    created_on = models.DateField(
        default=datetime.now, editable=False, null=True, blank=True
    )

    class Meta:
        verbose_name = "Actress Images"
        verbose_name_plural = "Actress Images"

    def __str__(self):
        return self.movie.name

class Slider(models.Model):
    objects = models.Manager

    image = models.ImageField(upload_to= 'slider/')

      # default Column

    is_active = models.BooleanField(default=True,editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )
    created_on = models.DateField(
        default=datetime.now, editable=False, null=True, blank=True
    )

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Slider"

    def __str__(self):
        return self.image.url