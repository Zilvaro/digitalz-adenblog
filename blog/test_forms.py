from django.test import TestCase
from .forms import AddPostForm


class TestAddPostForm(TestCase):

    def test_post_title_is_required(self):
        form = AddPostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'], [0], 'This field is required.')

    def test_content_field_is_not_required(self):
        form = AddPostForm({'content': ''})
        self.assertTrue(form.is_valid())

    def test_created_on_field_is_not_visible(self):
        form = AddPostForm()
        self.assertNotEqual(form.Meta.fields['created_on'])