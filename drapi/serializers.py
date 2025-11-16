from rest_framework import serializers
from .models import Aiquest

class AiquestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aiquest
        fields = "__all__"
#ei create function ar madhame , data add korle atomatic ekta instant database create hobe..
    def create(self , validated_data):
        return Aiquest.objects.create(**validated_data)