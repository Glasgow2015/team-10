from django.conf.urls import patterns, include, url
from volunteers.views import VolunteerList, VolunteerRegistration

urlpatterns = patterns(
    url(r'^$', VolunteerList.as_view(), name='volunteer-list'),
    url(r'^register/$', VolunteerRegistration.as_view(), name='volunteer-registration'),
)
