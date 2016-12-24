from django.db import models

# Create your models here.

class Product(models.Model):
    CREATED = 'CR'
    ACCEPTED = 'AC'
    MOVING = 'MV'
    RECEIVED = 'RC'
    DELIVEY_STATUS_CHOISES = (
        (CREATED, 'Created'),
        (ACCEPTED, 'Accepted'),
        (MOVING, 'Moving'),
        (RECEIVED, 'Received'),
    )
    name = models.CharField(max_length=50)
    count = models.IntegerField()
    address = models.CharField(max_length=100)
    date = models.DateField()
    deliveryStatus = models.CharField(
        max_length=2,
        choices=DELIVEY_STATUS_CHOISES,
        default=CREATED,
    )

    def __str__(self):
        return self.name + " " +  str(self.date) + " " + self.get_deliveryStatus_display()
