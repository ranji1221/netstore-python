from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func,home_page)
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		#self.assertTrue(response.content.startswith(b'<html>'))
		#self.assertIn(b'<title>To-Do lists</title>',response.content)
		#self.assertTrue(response.content.endswith(b'</html>'))
		excepted_html = render_to_string('home.html')  #响应的内容本来是字节，转为字符串方便测试
		self.assertEqual(response.content.decode(),excepted_html)
		
		self.assertTrue(excepted_html.startswith('<html>'))
		self.assertIn('<title>To-Do lists</title>',excepted_html)
		self.assertTrue(excepted_html.endswith('</html>'))