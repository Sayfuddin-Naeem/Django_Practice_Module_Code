from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class InstrumentTypeModel(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class MusicianModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    instrument_type = models.ManyToManyField(InstrumentTypeModel)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
class AlbumModel(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(
            MusicianModel,
            verbose_name=_("Musician of the Album"),
            on_delete=models.CASCADE
        )
    release_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    
    def __str__(self) -> str:
        return f"{self.album_name} - {self.musician.first_name}"