from rest_framework import viewsets
from .serializers import MemberSerializer, ActivityPeriodSerializer
from activity.models import UserProfile, ActivityPeriod
from django.http import JsonResponse

#class for displaying members
class MemberViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = MemberSerializer

#class for taking activity input
class ActivityPeriodViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer
