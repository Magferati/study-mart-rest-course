from rest_framework import serializers
from .models import Aiquest

class AiquestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aiquest
        fields = "__all__"
#ei create function ar madhame , data add korle atomatic ekta instant database create hobe..
    def create(self , validated_data):
        return Aiquest.objects.create(**validated_data)
    

#we use instance cuz it store previous data to database
#validated data change koro data gula save kore rakhe
    def update(self, instance, validate_data):
        instance.teacher_name = validate_data.get('teacher_name', instance.teacher_name)
        instance.course_name = validate_data.get('course_name', instance.course_name)
        instance.course_time = validate_data.get('course_time', instance.course_time)
        instance.seat = validate_data.get('seat', instance.seat)
        instance.save()
        return instance