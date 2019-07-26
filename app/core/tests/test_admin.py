from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse  # helper func allow generate URLs


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@sfadmin.com',
            password='pass123'
        )
        self.client.force_login(self.admin_user)
        # spare user to use for testing listing and others
        self.user = get_user_model().objects.create_user(
            email='test@sfcoder.com',
            password='pass1234',
            name='Test coder user'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
