from musicians_directory_app.models import *
from django.forms import ModelForm

class MusicianForm(ModelForm):
    class Meta:
        model = MusicianModel
        fields = '__all__'

class AlbumForm(ModelForm):
    class Meta:
        model = AlbumModel
        fields = ['album_name', 'musician', 'rating']