import os
from pathlib import Path
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from digital_defense import models

_prefix = Path(__file__).resolve(strict=True).parent.parent


class WebsiteViewSetTestCase(TestCase):

    fixtures = [
        f'{_prefix}/fixtures/ddi.json',
    ]

    def setUp(self):
        self.client = APIClient()

    def test_list(self):
        response = self.client.get('/websites/')
        count = models.Website.objects.count()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(count, len(response.json()))

    def test_retrieve(self):
        obj_id = 1
        obj = models.Website.objects.filter(id=obj_id).first()
        response = self.client.get(f'/websites/{obj_id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(obj.name, response.json().get('name'))


class PageViewSetTestCase(TestCase):

    fixtures = [
         f'{_prefix}/fixtures/ddi.json',
    ]

    def setUp(self):
        self.client = APIClient()

    def test_list(self):
        web_id = 1
        response = self.client.get('/pages/', {'website_id': 1})
        count = models.Page.objects.filter(website_id=web_id).count()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(count, len(response.json()))

    def test_retrieve(self):
        obj_id = 1
        obj = models.Page.objects.filter(id=obj_id).first()
        response = self.client.get(f'/pages/{obj_id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(obj.id, response.json().get('id'))
