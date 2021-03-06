"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from digital_defense import viewsets as dd_viewsets
from health import views as health_views


# Setup the URLs and include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),

    # Applications Urls
    path('health/', health_views.HealthCheckEndpoint.as_view(), name='health'),
    url(r'^ports/', include(dd_viewsets.ports_challenge_router.urls)),
    url(r'^pages/', include(dd_viewsets.page_site_router.urls)),
    url(r'^websites/', include(dd_viewsets.web_site_router.urls)),
    url(r'^vulnerabilities/', include(
        dd_viewsets.vulnerability_site_router.urls))
]
