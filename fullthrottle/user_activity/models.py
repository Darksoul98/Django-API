from django.db import models
import uuid
# Create your models here.
class UserInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    real_name = models.CharField(max_length=300)
    tz = models.CharField(max_length=300)

class Activity(models.Model):
    user = models.ForeignKey(
        'UserInfo',
        on_delete=models.CASCADE,
        related_name='activity_periods'
    )
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)