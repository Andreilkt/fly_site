from django.contrib import admin
from django.db import models
from fly_nsk.models import Betasevis, BetasevisText

#from fly.fly_nsk.models import BetasevisText BetasevisText

@admin.register(Betasevis)
class BetasevisAdmin(admin.ModelAdmin):
    list_display = ("main", "services", "works", "forms", "contacts", "site", "outsorcing")

@admin.register(BetasevisText)
class BetaservisTextAdmin(admin.ModelAdmin):
    list_display = ("main_text", "services_text", "works_text", "forms_text", "contacts_text", "site_text", "outsorcing_text")

