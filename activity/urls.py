from django.urls import include, path
from rest_framework import routers
from . import views

#creating router for api navigation
router = routers.DefaultRouter()
router.register(r'member', views.MemberViewSet,basename ='Member')
router.register(r'activity', views.ActivityPeriodViewSet,basename ='ActivityPeriod')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]