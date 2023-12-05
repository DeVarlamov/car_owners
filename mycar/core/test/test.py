from http import HTTPStatus

from django.test import Client, TestCase


class ViewTestClass(TestCase):
    """Фикстура создания клиента"""
    def setUp(self):
        self.client = Client()

    def test_error_page(self):
        """Тест на 404 ошибку и проверку HTML"""
        response = self.client.get('/nonexist-page/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        self.assertTemplateUsed(response, 'core/404.html')
