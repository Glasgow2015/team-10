from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'password',)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    password = serializers.CharField(required=True, write_only=True, style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if not user.is_active:
                msg = _('Your account is disabled')
                raise ValidationError(msg)
            attrs['user'] = user
            return attrs
        else:
            msg = _('Email or password is incorrect')
            raise ValidationError(msg)