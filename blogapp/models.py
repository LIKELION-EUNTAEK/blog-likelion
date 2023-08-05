from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    job = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.name}({self.id})'
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    importance = models.BooleanField(default=False)
    writing_time = models.DateTimeField(auto_now=True)
    post_photo = models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return f'{self.title}({self.id})'
    
    
class Comment(models.Model):
   # post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
   # created_at = models.DateTimeField(auto_now_add=True)
    

    

    

