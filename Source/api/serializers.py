from rest_framework import serializers

from api.models import Risk

class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields =  '__all__'