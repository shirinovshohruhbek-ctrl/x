from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('matn', 'rasm', 'audio', 'musiqa', 'fayl', 'video')