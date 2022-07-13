from rest_framework import serializers
from .models import *


class MenuSerializer(serializers.Serializer):
    """Creates serializer for menu"""

    title_link = serializers.CharField()
    url_link = serializers.CharField()


class ArticleSerializer(serializers.ModelSerializer):
    """Creates serializer for article"""

    class Meta:
        model = Article
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    """Creates serializer for Unit"""
    class Meta:
        model = Unit
        exclude = ('slug',)


class CastleSerializer(serializers.ModelSerializer):
    """Creates serializer for Castle"""
    castle = UnitSerializer(many=True, read_only=True)

    class Meta:
        model = Castle
        fields = ('title', 'description', 'castle')
