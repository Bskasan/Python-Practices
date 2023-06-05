from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        exclude = [
            # 'password',
            'date_joined',
            'groups',
            'last_login',
            'user_permissions',
        ]

        def validate(self, attrs):
          from django.contrib.auth.hashers import make_password # encryption function = Sifreleme fonks.
          from django.contrib.auth.password_validation import validate_password # validation function for your password
          
          password = attrs['password']
          validate_password(password)
          attrs.update(
            {
                'password' : make_password(password) # Encryption and update password.
            }
          )
        
          return super().validate(attrs)