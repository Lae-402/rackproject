from django.forms import ModelForm
from .models import Rack, Artist

class RegisterForm(ModelForm):
    class Meta:
        model = Rack
        fields = ['media', 'title', 'ruby', 'artist']

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['title']