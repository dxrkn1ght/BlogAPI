from rest_framework import serializers
from .models import Tag
from django.utils.text import slugify


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

    def create(self, validated_data):
        validated_data['slug'] = validated_data.get('slug') or slugify(validated_data['name'])
        return super().create(validated_data)