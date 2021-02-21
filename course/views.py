from django.shortcuts import render
from rest_framework.views import APIView
from .models import Course
from .seriallizers import getAllCourseOfViewSerializers
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class GetAllApiOfView(APIView):

    def get(self, request):
        list_course = Course.objects.all()
        my_data = getAllCourseOfViewSerializers(list_course, many=True)
        return Response(data=my_data.data, status=status.HTTP_200_OK)