from django.forms import ModelForm
from .models import Players


class PlayersForm(ModelForm):
    class Meta:
        model = Players
        # fields=['']
        fields = "__all__"