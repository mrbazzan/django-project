from django.db import models

# Create your models here.


class Order(models.Model):
    order_id = models.CharField(primary_key=True, max_length=255)
    date_created = models.DateTimeField()
    total_amount = models.CharField(max_length=255)

    STATUS_TYPE_CHOICE = [
        ('0', 'unpaid'),
        ('1', 'paid'),
        ('2', 'done'),
        ('-1', 'cancelled'),
    ]

    status = models.CharField(max_length=2, choices=STATUS_TYPE_CHOICE)

