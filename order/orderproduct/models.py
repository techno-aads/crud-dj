from django.db import models

class OrderProd(models.Model):
	order_title=models.CharField(max_length=100)
	order_count=models.IntegerField(default=0)
	order_address=models.CharField(max_length=200)
	order_date=models.DateTimeField('order date')
	oredr_status=models.CharField(max_length=11, default="не выполнен")
	def __str__(self):
		return self.order_title
