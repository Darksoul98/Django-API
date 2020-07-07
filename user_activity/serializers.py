from rest_framework.serializers import ModelSerializer
from user_activity.models import UserInfo, Activity

class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = ('start_time','end_time')

class UserSerializer(ModelSerializer):
    activity_periods = ActivitySerializer(many=True)
    class Meta:
        model = UserInfo
        fields = ("id","real_name","tz","activity_periods")
