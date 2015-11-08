from rest_framework.serializers import ModelSerializer
from volunteers.models import Volunteer


class VolunteerSerializer(ModelSerializer):
    class Meta:
        model = Volunteer