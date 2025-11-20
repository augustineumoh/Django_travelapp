from django.db import models
from rest_framework import serializers
from django.contrib.auth import get_user_model
# Create your models here.


User= get_user_model()

class Location(models.Model):
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.country} {self.city}'
    

class Booking(models.Model):
    TRIP_TYPE=(
        ('one_way','One Way'),
        ('round_trip','Round Trip'),
        ('multi_city','Multi City'),
    )
    FLIGHT_CLASSES=(
        ('economy', 'Economy'),
        ('premium', 'Premium Economy'),
        ('buisness', 'Buisness'),
        ('first_class', 'First Class'),
    )
    customer=models.ForeignKey(User, related_name='customer_booking', on_delete=models.CASCADE)
    agent=models.ForeignKey(User, related_name='agent_bookings', on_delete=models.SET_NULL, null=True, blank=True)

    trip_type= models.CharField(max_length=20, choices=TRIP_TYPE)
    travel_class=models.CharField(max_length=20, choices=FLIGHT_CLASSES)

    origin=models.ForeignKey(Location, related_name='origin_bookings', on_delete=models.CASCADE)
    destination=models.ForeignKey(Location, related_name='destination_bookings', on_delete=models.CASCADE)


    depart_date=models.DateField()
    return_date=models.DateField(null=True, blank=True)

    number_of_travelers=models.PositiveIntegerField(default=1)

    service=models.CharField(max_length=255)
    date=models.DateField()

    status=models.CharField(max_length=50, default='pending')

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer} | {self.trip_type} | {self.service}'
    
class MultiCitySegment(models.Model):
    booking=models.ForeignKey(Booking, related_name='segments', on_delete=models.CASCADE)
    origin= models.ForeignKey(Location,related_name='segment_origin', on_delete=models.CASCADE)
    destination=models.ForeignKey(Location, related_name='segment_destination', on_delete=models.CASCADE)
    depart_date=models.DateField()

    def __str__(self):
        return f'{self.origin}-{self.destination}'