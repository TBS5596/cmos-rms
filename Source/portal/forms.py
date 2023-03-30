from django.forms import ModelForm, DateInput
from api.models import Risk


class RiskForm(ModelForm):
    class Meta:
        model = Risk
        fields = '__all__'
        widgets = {
            'review_date': DateInput(attrs={'type': 'date'})
        }

class UpdateRiskMPForm(ModelForm):
    class Meta:
        model = Risk
        fields = ['likelihood', 'status', 'impact', 'mitigation_plan']