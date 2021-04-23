from rest_framework import serializers

from .models import Affair

class AffairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affair
        fields = ('id','affair')