from django.db import models

# Create your models here.

class Show(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    duration = models.IntegerField()
    date = models.DateTimeField()
    advertisement = models.BooleanField()

    def __add__(self, other):
        self.name = other
        self.save()


    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()


    # author = models.ForeignKey('auth.User')
    # title = models.CharField(max_length=200)
    # text = models.TextField()
    # created_date = models.DateTimeField(
    #         default=timezone.now)
    # published_date = models.DateTimeField(
    #         blank=True, null=True)
    #
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()
    #
    # def __str__(self):
    #     return self.title