from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    number = serializers.IntegerField()