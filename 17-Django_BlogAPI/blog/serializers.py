from rest_framework import serializers
from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = [
            # 'created_date'
            # 'updated_date'
        ]