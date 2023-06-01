from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all(), message='Email is not unique!')]
    )

    password = serializers.CharField(
        required = True,
        write_only = True, # Not going Front-end
        validators = [validate_password] # Djando validation itself
    )

    password2 = serializers.CharField(
        required = True,
        write_only = True, # Not going Front-end
    )

    class Meta:
        model = User
        # Which field will be seen to save database
        fields = ['username', 'password', 'password2', 'email']
        # To-dos
        # - Sign up with email and password
        # - Email needs to be unique
        # - Write passwrod 2 times
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password':"Password doesn't match!"})

        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data.get('username'),
            email = validated_data.get('email'),
        )

        user.set_password(validated_data.get('password'))
        user.save()

        return user