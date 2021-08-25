from django.test import TestCase, Client, LiveServerTestCase, SimpleTestCase
from django.urls import *
from Trequest.models import *
import json

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
#from Tserasp import Trequest

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from Trequest.forms import *
from django.core.mail import send_mail


class TestViews(TestCase):
    # testing home page is working
    def test_home_status(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
    # testing account template  is working

    def test_correct_template(self):
        response = self.client.get(reverse('account'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Trequest/account_management.html')

    # def test_project_material_request(self):
    #     client = Client()
    #     response = client.get(reverse('make-request'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'Trequest/make_request.html')

    # def test_project_material(self):
    #     client = Client()
    #     response = client.get(reverse('AddMaterial'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'Trequest/add_material_form.html')
