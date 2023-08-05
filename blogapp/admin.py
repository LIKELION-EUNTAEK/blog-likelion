from django.contrib import admin

from blogapp.models import Person, Post, Comment

# Register your models here.
admin.site.register(Person)
admin.site.register(Post)
admin.site.register(Comment)