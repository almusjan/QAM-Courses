from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Site)
admin.site.register(models.Course)
admin.site.register(models.Report)
admin.site.register(models.ReportReply)

admin.site.register(models.FavoriteSite)

