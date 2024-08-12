from django.urls import path
from musicians_directory_app.views import *

urlpatterns = [
    path('user/add/musician/', MusicianView.as_view(), name='add_musician'),
    path('user/edit/musician/<int:id>', EditMusicianView.as_view(), name='edit_musician'),
    path('user/add/album/', AlbumView.as_view(), name='add_album'),
    path('user/edit/album/<int:id>', EditAlbumView.as_view(), name='edit_album'),
    path('user/delete/album/<int:id>', AlbumDeleteView.as_view(), name='delete_album'),
]