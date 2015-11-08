from rest_framework.generics import ListAPIView, CreateAPIView
from volunteers.serializers import VolunteerSerializer
from volunteers.models import Volunteer


class VolunteerList(ListAPIView):
    serializer_class = VolunteerSerializer
    queryset = Volunteer.objects.all()


class VolunteerRegistration(CreateAPIView):
    serializer_class = VolunteerSerializer
    queryset = Volunteer.objects.all()