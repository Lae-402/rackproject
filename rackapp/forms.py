from django.forms import ModelForm
from .models import Rack

class RegisterForm(ModelForm):
    class Meta:
        model = Rack
        fields = ['media', 'title', 'ruby', 'artist']