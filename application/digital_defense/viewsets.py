import requests
import itertools
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import response
from rest_framework import routers

from core import helpers

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


class PortsViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for testing port challenge
    """

    def create(self, request):
        # case 1
        # include_ports = [[80, 80], [22, 23], [8000, 9000]]
        # exclude_ports = [[8080, 8080], [1024, 1024]]

        # case 2
        include_ports = [[8000, 9000], [80, 80], [22, 23]]
        exclude_ports = [[1024, 1024], [8080, 8080]]

        # case 3
        # include_ports = [[1, 65535]]
        # exclude_ports = [[1000, 2000], [500, 2500]]

        ports_result = []

        for inc_port in include_ports:
            for exc_port in exclude_ports:
                if inc_port[0] <= exc_port[0] <= inc_port[1]:
                    inc_range = list(range(inc_port[0], inc_port[1]+1))
                    exc_range = list(range(exc_port[0], exc_port[1]+1))

                    set_difference = set(inc_range) - set(exc_range)
                    list_difference = list(set_difference)
                    ports_result.append(list_difference)
                else:
                    ports_result.append(list(inc_port))

        ports_result = set(item for pair in ports_result for item in pair)
        ports_result = sorted(ports_result)


        return response.Response(data=helpers.intervals_extract(ports_result))


ports_challenge_router = routers.SimpleRouter()
ports_challenge_router.register(
    '',
    PortsViewSet,
    basename='port-challenge')
