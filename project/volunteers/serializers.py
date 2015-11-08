from rest_framework.serializers import ModelSerializer
from volunteers.models import Volunteer


class VolunteerSerializer(ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ('first_name', 'last_name', 'city', 'phone_number',
                  'email', 'date_of_birth', 'subscribed_to_newsletter')