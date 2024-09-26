from django.contrib import admin
from django.forms import ModelForm
from django.http import HttpRequest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .models import Comment, Category, Post, Setting

class BlogAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_display = ['name']
    
    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except IntegrityError:
            form.add_error('slug', ValidationError("error"))
            return 
        super().save_model(request, obj, form, change)
      
    
class CategorysAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_display = ['name']
    
    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except IntegrityError:
            form.add_error('slug', ValidationError("error"))
            return 
        super().save_model(request, obj, form, change)
        
            
    
    
admin.site.register(Post, BlogAdmin)
admin.site.register(Category, CategorysAdmin)
admin.site.register(Comment)
admin.site.register(Setting)