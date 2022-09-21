from django.test import TestCase
from .models import HeroContent

class TestViews(TestCase()):

    def test_get_add_content_page(self):
        response = self.client.get('/add_content')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_content.html')



