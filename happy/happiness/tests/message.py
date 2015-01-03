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


    def test_message_view(self):
        '''
        Tests for the message view
        '''
        message_prv = MessageFactory(privacy='prv')
        message_pub = MessageFactory(privacy='pub')

        request = self.client.get('/messages/')
        messages = request.data['results']
        for msg in messages:
            if msg['privacy'] == 'prv':
                self.assertEqual(msg['author'], 'anonymous')
            else:
                self.assertIsNotNone(msg['author']['username'])
