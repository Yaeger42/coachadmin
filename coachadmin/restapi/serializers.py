from rest_framework import serializers
from coach.models import Coach

class CoachSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Coach
        fields = ('firstName', 'lastName', 'email', 'phone', 'location', 'hobby')