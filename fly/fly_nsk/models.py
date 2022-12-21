from django.conf import settings
from django.db import models
from django.utils import timezone


class Betasevis(models.Model):
    main = models.TextField()
    services = models.TextField()
    works = models.TextField()
    forms = models.TextField()
    contacts = models.TextField()
    site = models.TextField()
    outsorcing = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)

def __str__(self):
    return f"{self.main}, {self.services}, {self.works}, {self.forms}, {self.contacts}, {self.site}, {self.outsorcing}"

class BetasevisText(models.Model):
    main_text = models.TextField()
    services_text = models.TextField()
    works_text = models.TextField()
    forms_text = models.TextField()
    contacts_text = models.TextField()
    site_text = models.TextField()
    outsorcing_text = models.TextField()
    Betasevis = models.OneToOneField(Betasevis, on_delete=models.CASCADE, primary_key=True)
def __str__(self):
    return f"{self.main_text}, {self.services_text}, {self.works_text}, {self.forms_text}, {self.contacts_text}, {self.site_text}, {self.outsorcing_text}"

"""
    def publish(self):
        self.published_date = timezone.now()
        self.save()
"""


