from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
      model = Album
      fields = [
        'album_title',
        'artist_name',
        'date_released',]


    


    widgets = {
    'date_released': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }