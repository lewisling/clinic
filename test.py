from django.core.urlresolvers import resolve
from django.test import TestCase
from notetaker.views import home_page

class HomePageTest(TestCase):
	def test_root_url_to_resolves_to_homepage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
