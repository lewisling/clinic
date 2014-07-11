from django.core.urlresolvers import resolve
from django.test import TestCase, LiveServerTestCase, Client
from django.http import HttpRequest
from notetaker.views import home_page
from notetaker.views import register_page
from notetaker.views import newnote_page
from notetaker.views import addpatient_page
from notetaker.models import Note
from notetaker.models import UserProfile
from django.template.loader import render_to_string
from django.utils import timezone
from django.contrib.auth.models import User

class HomePageTest(TestCase):
    def test_root_url_to_resolves_to_homepage_view(self):
        found = resolve('/')        
        self.assertEqual(found.func, home_page)
    #
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>log in</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        #
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
    #
    def test_register_page_returns_correct_html(self):
        request = HttpRequest()
        response = register_page(request)
        #self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>register</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        #
        expected_html = render_to_string('register.html')
        self.assertEqual(response.content.decode(), expected_html)
    #
    def test_newnote_page_returns_correct_html(self):
        request = HttpRequest()
        response = newnote_page(request)
        #self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>new_note</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        #
        expected_html = render_to_string('newnote.html')
        self.assertEqual(response.content.decode(), expected_html)
    #
    def test_addpatient_page_returns_correct_html(self):
        request = HttpRequest()
        response = addpatient_page(request)
        #self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>add_patient</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        #
        expected_html = render_to_string('addpatient.html')
        self.assertEqual(response.content.decode(), expected_html)
    #

class ModelTest(TestCase):
    def test_create_note(self):
        note1 = Note()
        note1.text = "This is a patient note."
        note1.date = timezone.now()
        note1.save()
        saved_notes = Note.objects.all()
        self.assertEqual(saved_notes.count(),1)
        first_note = saved_notes[0]
        #second_note= saved_notes[1]
        self.assertEqual(first_note.text,"This is a patient note.")
        self.assertEquals(first_note.date,note1.date)
        
    def test_create_users(self):
        user1 = UserProfile()
        user1.first_name = "user first"
        user1.last_name = "user last"
        user1.user_type = 'P'
        user1.user_id = '1'
        user1.save()
        saved_users = UserProfile.objects.all()
        self.assertEqual(saved_users.count(),1)
        first_user = saved_users[0]
        self.assertEqual(first_user.first_name, "user first")
        self.assertEquals(first_user.last_name, user1.last_name)
        

class AdminTest(LiveServerTestCase):
    def test_login(self):
        self.client = Client()
        self.username = 'user2'
        self.email = 'test@test.com'
        self.password = 'user2'        
        self.test_user = User.objects.create_user(self.username, self.email, self.password)
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
        #response = self.client.get('/admin/logout')
        #print response.content
        #self.assertIn('/admin/logout/', response.content)