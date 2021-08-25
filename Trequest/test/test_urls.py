from django.test import SimpleTestCase
from Trequest.views import *
from Trequest.urls import *
from TSERASP.urls import *
from django.urls import *


class TestUrls(SimpleTestCase):
    # test login url
    def test_list_login_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, signin)
    # test index url

    def test_list_index_is_resolved(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)
    # test register url

    def test_list_register_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, create_account)
    # test profile url

    def test_list_profile_is_resolved(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)
    # test accoount managment url

    def test_list_account_is_resolved(self):
        url = reverse('account')
        print(resolve(url))
        self.assertEquals(resolve(url).func, account_management)

    # test edit account url

    def test_list_edit_account_is_resolved(self):
        url = reverse('edit-account')
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_account)
    # test detail account url

    def test_list_detail_account_is_resolved(self):
        url = reverse('detail-account', args=['some-int'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, account_detail)
    # test logout url

    def test_list_logout_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, user_logout)
    # test change password url

    def test_list_change_password_is_resolved(self):
        url = reverse('change-password')
        print(resolve(url))
        self.assertEquals(resolve(url).func, change_password)
    # test tsho view request url

    def test_list_tsho_view_request_is_resolved(self):
        url = reverse('tsho-view-request')
        print(resolve(url))
        self.assertEquals(resolve(url).func, tsho_view_request)
