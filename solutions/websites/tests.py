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
        response = self.client.get(f'/pages/?website_id={web_id}')
        count = models.Page.objects.filter(website_id=web_id).count()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(count, len(response.json()))

    def test_retrieve(self):
        obj_id = 1
        obj = models.Page.objects.filter(id=obj_id).first()
        response = self.client.get(f'/pages/{obj_id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(obj.id, response.json().get('id'))


class VulnerabilityViewSetTestCase(TestCase):

    fixtures = [
         f'{_prefix}/fixtures/ddi.json',
    ]

    def setUp(self):
        self.client = APIClient()

    def test_list(self):

        response = self.client.get('/vulnerabilities/')
        count = models.Vulnerability.objects.all().count()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(count, len(response.json()))

    def test_foo_login(self):

        """
        Test Condition from specifictions
        Input:
            All vulnerabilities for foo.com on login.html page
        Output:
            1, 1, SQL injection response blah
            2, 1, XXE response
            3, 1, Stored XSS response
        """

        foo_id = 1
        foo_obj = models.Website.objects.filter(id=foo_id).first()
        page_obj = models.Page.objects.filter(
            website_id=foo_obj.id).first()

        response = self.client.get(
            f'/vulnerabilities/?website_id={page_obj.id}')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        result = False
        for vulnerability in response.json():
            if any(
                [
                    vulnerability.get('data') == 'SQL injection response blah',
                    vulnerability.get('data') == 'XXE response',
                    vulnerability.get('data') == 'Stored XSS response'
                ]
            ):
                result = True
        self.assertEqual(True, result)
