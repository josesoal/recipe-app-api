from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        '''Setup run before every test method'''
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@tempo.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@tempo.com',
            password='password123',
            name='Test User Full Name',
        )

    def test_users_listed(self):
        """Test that users are listed on the user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    '''NOTE:
    When an AdminSite is deployed, the views provided by that site are
    accessible using Django’s URL reversing system.

    Eachs ModelAdmin instace provides a set of Named-URLs, in this case
    one of those named-URLs is core_user_changelist and corresponds to
    the Changelist page.

    Check the official doc at:
    docs.djangoproject.com/en/4.0/ref/contrib/admin/#reversing-admin-urls
    '''

    def test_user_page_change(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
