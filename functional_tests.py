from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()       #需要下载chrome浏览器的驱动，并在环境变量path中指定
		#self.browser = webdriver.Firefox()		#需要下载firefox浏览器的驱动，并在环境变量path中指定
		self.browser.implicitly_wait(3)      #如果用火狐浏览器似乎这个代码有个bug
	def setDown(self):
		self.browser.quit()
	def test_can_start_a_list_and_retrieve_it_later(self):
		#伊迪斯听说有一个很酷的在线待办事项应用
		#她去看了这个应用的首页
		self.browser.get('http://localhost:8000')

		#她注意到网页的标题和头部都包含了"To-Do"这个词
		self.assertIn('To-Do',self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',headerText)
		self.fail('Finish the test!')
		
		#应用邀请她输入一个待办事项
		inputBox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputBox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		
		#她在一个文本框中输入了"Buy peacock feathers"(购买孔雀羽毛)
		#伊迪斯的爱好是使用假蝇做鱼饵钓鱼
		inputBox.send_keys('Buy peacock feathers')
		
		#她按回车键后，页面更新了
		#待办事项表格中显示了"1: Buy peacock feathers"
		inputBox.send_keys(Keys.ENTER)
		
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows)
		)
		
		#页面中又显示了一个文本框，可以输入其他的待办事项
		#她输入了"Use peacock feathers to make a fly"(使用孔雀羽毛做假蝇)
		#伊迪斯做事儿很有条理
		self.fail('Finish the test!')
		
		#页面再次更新，她的清单中显示了这两个待办事项
		[...]
		
		#她很满意，去睡觉了
		
if __name__ == '__main__':
	unittest.main()

