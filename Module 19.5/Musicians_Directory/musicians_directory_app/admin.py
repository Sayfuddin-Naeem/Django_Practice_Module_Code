from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.MusicianModel)
admin.site.register(models.AlbumModel)
admin.site.register(models.InstrumentTypeModel)
