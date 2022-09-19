from django.test import TestCase
from .models import HeroContent

class TestViews(TestCase()):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


    


    
