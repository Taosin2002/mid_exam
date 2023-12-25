from django.db import models
from category.models import Category
# Create your models here.
class CarModel(models.Model):
    image=models.ImageField(upload_to='author/media/',blank = True, null = True)
    name=models.CharField(max_length=150)
    discription=models.TextField()
    quantity=models.IntegerField()
    price=models.IntegerField()
    brand_name=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"
    