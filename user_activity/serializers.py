from rest_framework.serializers import ModelSerializer
from user_activity.models import UserInfo, Activity
from rest_framework import serializers

class ActivitySerializer(serializers.Serializer):
    # class Meta:
    #     model = Activity
    #     fields = ('start_time','end_time')
    start_time = serializers.DateTimeField(format="%b %d %Y %I:%M %p")
    end_time = serializers.DateTimeField(format="%b %d %Y %I:%M %p")


class UserSerializer(ModelSerializer):
    activity_periods = ActivitySerializer(many=True)
    class Meta:
        model = UserInfo
        fields = ("id","real_name","tz","activity_periods")
