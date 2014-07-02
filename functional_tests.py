from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
class newUserLogin(unittest.TestCase):
	def setup(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	def teardown(self):
		self.browser.quit()	
	def test_can_start_notetaker_and_retireve_login_page(self):
		browser.get('http://localhost:8000')
		self.assertIn('log in', self.browser.title)
		#
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('log in', header_text)
		#
		usrnme_inputbox = self.browser.find_elemnet_by_id('id_login_name')
		self.assertEqual(usrnme_inputbox.get_attribute('name_placeholder), 'Enter login name')
		usrnme_inputbox.send_keys('Jane Doe')
		usrnme_inputbox.send_keys(keys.ENTER)
		#
		pwd_inputbox = self.browser.find_elemnet_by_id('id_login_pwd')
		self.assertEqual(pwd_inputbox.get_attribute('pwd_placeholder), 'Enter login name')
		pwd_inputbox.send_keys('whatever')
		pwd_inputbox.send_keys(keys.ENTER)
		#
		submit_button = self.browser.find_element_by_id('id_submit_btn')
		#
		wait = WebDriverWait( browser, 5 )
		#
		#page_loaded = wait.until_not(lambda browser: browser.current_url == login_page)
		#
		#except TimeoutException:
		#	self.fail( "Loading timeout expired" )
		#
		self.assertEqual(browser.current_url,correct_page,msg = "Successful Login")