from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import routers

from digital_defense import filters
from digital_defense import models
from digital_defense import serializers


class WebsiteViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing website objects.
    """
    queryset = models.Website.objects.all()
    serializer_class = serializers.WebsiteSerializer
    permission_classes = [permissions.AllowAny]


web_site_router = routers.SimpleRouter()
web_site_router.register('', WebsiteViewSet, basename='websites')


class PageViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing page objects.
    """
    queryset = models.Page.objects.all()
    serializer_class = serializers.PageSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.PagesFilterByWebsite]


page_site_router = routers.SimpleRouter()
page_site_router.register('', PageViewSet, basename='pages')


class VulnerabilityViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing vulnerability objects.
    """
    queryset = models.Vulnerability.objects.all()
    serializer_class = serializers.VulnerabilitySerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.VulnerabilityFilterByWebsite]


vulnerability_site_router = routers.SimpleRouter()
vulnerability_site_router.register(
    '',
    VulnerabilityViewSet,
    basename='vulnerabilities')
