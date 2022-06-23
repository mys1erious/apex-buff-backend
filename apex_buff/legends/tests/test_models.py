from django.test import TestCase
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch


class LegendModelTests(TestCase):
    def setUp(self) -> None:
        self.slug = 'some-slug'
        self.list_expected_url = '/api/v1/legends/'
        self.detail_expected_url = f'/api/v1/legends/{self.slug}/'

    def test_absolute_url_for_list_view(self):
        self.assertEqual(reverse('legends'), self.list_expected_url)

    def test_absolute_url_for_detail_view(self):
        self.assertEqual(reverse('legends', kwargs={'slug': self.slug}), self.detail_expected_url)

    def test_absolute_url_for_detail_view_with_non_slug_arg(self):
        self.assertRaises(
            NoReverseMatch,
            reverse, 'legends', kwargs={'pk': 1}
        )
        self.assertRaises(
            NoReverseMatch,
            reverse, 'legends', kwargs={'name': 'some-name'}
        )
