from rest_framework import serializers
from digital_defense import models


class WebsiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Website
        fields = [
            'id',
            'name',
            'url',
        ]


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Page
        fields = [
            'id',
            'website_id',
            'path',
        ]


class VulnerabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Vulnerability
        fields = [
            'id',
            'page_id',
            'data',
        ]
