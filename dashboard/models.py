from django.db import models
from django.utils.text import slugify
from django.db import IntegrityError
from django.core.exceptions import ValidationError

class Setting(models.Model):
    name = models.TextField()
    title = models.TextField()
    copyright = models.CharField(max_length=4)
    description = models.TextField(blank=True)
    keyword = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    photos = models.TextField(blank=True, null=True, default="https://shakibprotfolio.pages.dev/fav.png")
    tag = models.TextField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)
    descripton = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=100, default='', unique=True, blank=True, null=True)
    category = models.ForeignKey("Category", related_name="Post", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
            try:
                super(Post, self).save(*args, **kwargs)
            except IntegrityError:
                raise ValidationError('Error')
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    photos = models.TextField(blank=True, null=True, default="https://shakibprotfolio.pages.dev/fav.png")
    tag = models.TextField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)
    descripton = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=100, default='', unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            
        try:
            super(Category, self).save(*args, **kwargs)
        except IntegrityError:
            raise ValidationError(f"A category with the slug '{self.slug}' already exists. Please provide a unique slug.")  
    
    def __str__(self):
        return self.name
    
    
class Comment(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=100)
    parent = models.IntegerField(default=0)
    reply_to = models.IntegerField(default=0)
    post_id = models.IntegerField(default=1)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name