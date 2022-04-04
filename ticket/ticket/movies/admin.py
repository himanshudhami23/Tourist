from blogs import models
from django.contrib import admin
from .models import Category,Movies,Actress_Images,Slider
from django.utils.text import slugify
import os
# Register your models here.

def active_selected_record(self, request, queryset):
    queryset.update(is_active=True)

def inactive_selected_record(self, request, queryset):
    queryset.update(is_active=False)
    

class Actress_Image_Inline(admin.StackedInline):
    model = Actress_Images
    extra = 1

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name','is_active','created_by','created_on']
    search_fields = ['name']
    list_per_page = 10

    def save_model(self,request,obj,form,change):
        try:
           
            obj.created_by = request.user
            obj.url = slugify(obj.name)
            super().save_model(request,obj,form,change)
        except Exception as error:
            print(error)

class MoviesAdmin(admin.ModelAdmin):

    list_display = ['name','category','url','relished_date','is_active','created_by','created_on']
    search_fields = ['name']
    filter = ['category','is_active']
    list_per_page = 10
    inlines=[Actress_Image_Inline]
    
    def save_model(self,request,obj,form,change):
        try:
            obj.created_by = request.user
            obj.url = slugify(obj.name)
            if change:
                imgData = Movies.objects.get(pk=obj.id)

                if imgData.image != obj.image:
                    if os.path.exists(imgData.image.path):
                        os.remove(imgData.image.path)  

            super().save_model(request,obj,form,change)
        except Exception as error:
            print(error)

    def delete_model(self,request,obj):
        try:
            os.remove(obj.image.path)
            
            super().delete_model(request,obj)
        except Exception as er:
            print(er)

class SliderAdmin(admin.ModelAdmin):

    list_display = ['image','is_active','created_by','created_on']

    list_per_page = 10

    def save_model(self,request,obj,form,change):
        try:
           
            obj.created_by = request.user
            if change:
                imgData = Slider.objects.get(pk=obj.id)

                if imgData.image != obj.image:
                    if os.path.exists(imgData.image.path):
                        os.remove(imgData.image.path) 
            super().save_model(request,obj,form,change)
        except Exception as error:
            print(error)

admin.site.add_action(active_selected_record)
admin.site.add_action(inactive_selected_record)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Movies,MoviesAdmin)
admin.site.register(Slider,SliderAdmin)