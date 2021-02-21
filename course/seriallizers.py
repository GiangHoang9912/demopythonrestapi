from rest_framework import serializers
from .models import Course


class getAllCourseOfViewSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ('id' , 'title', 'prince', 'content')