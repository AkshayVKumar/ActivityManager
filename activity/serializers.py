from rest_framework import serializers
from activity.models import UserProfile, ActivityPeriod

#activity period serializer for activity period model
#used to take activity input
class ActivityPeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPeriod
        fields = [ 'member','start_time', 'end_time']
        

#this serializer is used to group the start time and endtime and
class ActivityPeriod2Serializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M %p')
    end_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M %p')
    class Meta:
        model = ActivityPeriod
        fields = [ 'start_time', 'end_time']     
    
#handles the members view details
class MemberSerializer(serializers.ModelSerializer):
    activity_period = ActivityPeriod2Serializer(many=True)
    class Meta:
        model = UserProfile
        fields = ['id','real_name', 'tz','activity_period']