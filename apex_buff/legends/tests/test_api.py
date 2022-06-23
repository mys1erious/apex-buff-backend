import json

from django.test import TransactionTestCase
from django.urls import reverse

from ..models import Legend


class LegendAPITests(TransactionTestCase):
    reset_sequences = True

    def setUp(self) -> None:
        Legend.objects.get_or_create(
            name='Some Name1',
            gender='m',
        )
        Legend.objects.get_or_create(
            name='Some Name2',
            gender='f',
        )

        self.list_url = reverse('legends')
        self.detail_url_obj_1 = reverse('legends', kwargs={'slug': 'some-name1'})

    def test_list(self):
        response = self.client.get(self.list_url)
        self.assertContains(response, 'Some Name1')
        self.assertContains(response, 'Some Name2')

    def test_detail(self):
        response = self.client.get(self.detail_url_obj_1)
        data = json.loads(response.content)
        content = {
            'name': 'Some Name1',
            'icon': '/media/no_image.png',
            'slug': 'some-name1',
            'role': '',
            'real_name': '',
            'gender': 'm',
            'age': None,
            'homeworld': '',
            'legend_type': None,
            'lore': '',
            'abilities': ''
        }
        self.assertEqual(data, content)

    def test_post(self):
        post_data = {'name': 'Some Name3', 'gender': 'f'}
        response = self.client.post(self.list_url, post_data)
        self.assertEquals(response.status_code, 201)

        data = json.loads(response.content)
        content = {
            'name': 'Some Name3',
            'icon': '/media/no_image.png',
            'slug': 'some-name3',
            'role': '',
            'real_name': '',
            'gender': 'f',
            'age': None,
            'homeworld': '',
            'legend_type': None,
            'lore': '',
            'abilities': ''
        }

        self.assertEquals(data, content)
        self.assertEquals(Legend.objects.count(), 3)

    def test_put(self):
        put_data = {'name': 'Some Name1 Updated', 'gender': 'nb'}
        response = self.client.put(self.detail_url_obj_1, put_data, content_type='application/json')
        self.assertEquals(response.status_code, 200)

        data = json.loads(response.content)

        content = {
            'name': 'Some Name1 Updated',
            'icon': '/media/no_image.png',
            'slug': 'some-name1-updated',
            'role': '',
            'real_name': '',
            'gender': 'nb',
            'age': None,
            'homeworld': '',
            'legend_type': None,
            'lore': '',
            'abilities': ''
        }

        self.assertEquals(data, content)
        self.assertEquals(Legend.objects.count(), 2)

    def test_delete(self):
        legend_obj1_name = Legend.objects.get(pk=1).name
        response = self.client.delete(self.detail_url_obj_1)
        self.assertEquals(response.status_code, 204)

        self.assertEquals(Legend.objects.count(), 1)
