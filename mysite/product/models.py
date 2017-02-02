from django.db import models

class InfoProd(models.Model):
    prod_title = models.CharField(max_length=100)
    prod_count = models.IntegerField(default=0)
    prod_address = models.CharField(max_length=200)
    prod_date = models.DateTimeField('prod_date')
    prod_status = models.BooleanField()

    def __str__(self):
        return self.prod_title
