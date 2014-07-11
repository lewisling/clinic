from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):  
	def setUp(self): 
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	#def tearDown(self):
		#self.browser.quit()
	def test_can_start_notetaker_and_retireve_login_page(self):  
		self.browser.get('http://localhost:8000')
		self.assertIn('log in', self.browser.title)
		#
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Your name and password', header_text)
		#
		usrnme_inputbox = self.browser.find_element_by_id('id_login_name')
		self.assertEqual(usrnme_inputbox.get_attribute('placeholder'),'name_placeholder')
		usrnme_inputbox.send_keys('Jane Doe')
		usrnme_inputbox.send_keys(Keys.ENTER)
		#
		pwd_inputbox = self.browser.find_element_by_id('id_login_pwd')
		self.assertEqual(pwd_inputbox.get_attribute('placeholder'), 'pwd_placeholder')
		pwd_inputbox.send_keys('whatever')
		pwd_inputbox.send_keys(Keys.ENTER)
		#
		submit_button = self.browser.find_element_by_id('id_submit_button')
if __name__ == '__main__':
	unittest.main(verbosity=2)