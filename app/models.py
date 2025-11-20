from django.db import models

# Create your models here.
class Trip(models.Model):
    destination=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['created_at']

    def __str__(self):
        return self.destination    