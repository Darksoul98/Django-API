from django.shortcuts import render
from user_activity.models import UserInfo, Activity 
from user_activity.serializers import UserSerializer
from rest_framework import generics
from rest_framework.response import Response
# Create your views here.
class UserList(generics.ListAPIView):
    queryset = UserInfo.objects.all() 
    serializer_class = UserSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        res ={
            "ok":True,
            "message":serializer.data
        }
        return Response(res)