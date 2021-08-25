from django.test import TestCase, Client
from django.urls import *
from Trequest.models import *
import json

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
#from Tserasp import Trequest
from sys import path_hooks
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.validators import ProhibitNullCharactersValidator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import PasswordChangeForm
from Trequest.forms import *
from django.core.mail import send_mail

from django.http.response import JsonResponse
import time
from django.test.runner import DiscoverRunner
from django.test.testcases import LiveServerTestCase



class TestProject(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.close()

    def test_project_alert_is_displayed(self):
        self.browser.get(self.live_server_url)

    def testhomepage(self):
        self.browser.get('http://127.0.0.1:8000/')
        username = self.browser.find_element_by_name('username')
        userpassword = self.browser.find_element_by_name('password')
        submit = self.browser.find_element_by_name('submit')
        time.sleep(3)
        username.send_keys('Admin')
        userpassword.send_keys('12345678')
        submit.send_keys(Keys.RETURN)
        assert 'admin' in self.browser.page_source
        self.browser.close(20)
