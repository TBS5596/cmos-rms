from django.forms import ModelForm
from api.models import Risk


class RiskForm(ModelForm):
    class Meta:
        model = Risk
        fields = '__all__'