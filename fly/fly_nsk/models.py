from django.conf import settings
from django.db import models
from django.utils import timezone


class Betasevis(models.Model):
    main = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    services = models.TextField()
    works = models.TextField()
    forms = models.TextField()
    contacts = models.TextField()
    forms = models.TextField()
    site = models.TextField()
    outsorcing = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title