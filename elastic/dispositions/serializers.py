from rest_framework import serializers

from .models import Disposition

class DispositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disposition
        fields = ('id','dispositionType')