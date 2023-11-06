from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    last_retrieved_at = models.DateTimeField(auto_now=True)
    retrieved_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
