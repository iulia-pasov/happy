from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIRequestFactory, APIClient
from rest_framework import status

from happiness.models import Message
from happiness.tests.factories import MessageFactory, UserFactory


class MessageViewTests(TestCase):
    '''
    Tests for the message view
    '''

    def setUp(self):
        super(MessageViewTests, self).setUp()

        self.messageContent = {
            'privacy': 'pub',
            'message_content': 'Everybody loves Iulia'
        }
        self.client = APIClient()
        user = UserFactory()

    def tearDown(self):
        Message.messages.all().delete()
        self.client.logout()

    def test_private_message_view(self):
        '''
        Tests for the message view
        '''
        message_prv = MessageFactory(privacy='prv')

        request = self.client.get('/messages/')
        message = request.data['results'][0]
        self.assertEqual(message['author'], 'anonymous')

    def test_public_message_view(self):
        """
        Test for public message
        """
        message_pub = MessageFactory(privacy='pub')
        request = self.client.get('/messages/')
        message = request.data['results'][0]
        self.assertNotEqual(message['author'], 'anonymous')
        self.assertEqual(message['author'], 'test')

    def test_post_message_as_auth(self):
        """
        Test if an authenticated user can post a message
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.post('/messages/', self.messageContent)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        message = self.client.get('/messages/').data['results'][0]
        self.assertEqual(message['author'], 'test')
        self.assertEqual(message['privacy'], 'pub')
        self.assertEqual(message['message_content'], 'Everybody loves Iulia')

    def test_post_message_as_anon(self):
        """
        Test if an anonymous user cannot post a message
        """
        response = self.client.post('/messages/', self.messageContent)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(self.client.get('/messages/').data['count'], 0)
 
    def test_edit_message_as_author(self):
        """
        Test if an authenticated user can edit his own message
        """

    def test_edit_message_as_anon(self):
        """
        Test if an anonymous user cannot edit a message
        """

    def test_edit_message_as_auth_not_author(self):
        """
        Test if an authenticated user cannot edit some other user's message
        """
