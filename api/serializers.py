from rest_framework import serializers
from .models import YieldPerKwp


class YieldPerKwpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = YieldPerKwp
        fields = ('yield_kWp', 'state')