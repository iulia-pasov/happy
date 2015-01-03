from django.test import TestCase

from happiness.models import Message
from happiness.tests.factories import MessageFactory


class MessageViewTests(TestCase):
    '''
    Tests for the message view
    '''

    def setUp(self):
        super(MessageViewTests, self).setUp()

    def tearDown(self):
        Message.messages.all().delete()


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
        self.assertIsNotNone(message['author']['username'])
