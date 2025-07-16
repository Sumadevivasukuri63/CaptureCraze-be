from django.db import models

class Photographer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    def __str__(self):
        return self.name

class Booking(models.Model):
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_type = models.CharField(max_length=50)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer_name} - {self.event_type} on {self.event_date}"
