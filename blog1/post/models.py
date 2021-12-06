from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Blog(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=500, help_text='title', blank=False, null=False)
    body = RichTextField(blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.pk)])


class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=13, blank=False, null=False)
    email = models.EmailField(max_length=255, null=True, blank=True)
    message = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name