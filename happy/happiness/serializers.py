from django.contrib.auth.models import User

from rest_framework import serializers

from happiness.models import Message


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    """
    Simple message serializer
    """

    def create(self, validated_data):
        """
        Create and return a new Message instance
        """
        request = self.context.get('request', None)
        if request is not None:
            user = request.user
            validated_data['author'] = user
        return Message.messages.create(**validated_data)

    def to_representation(self, instance):
        data = super(MessageSerializer, self).to_representation(instance)
        if data['privacy'] == 'prv':
            data['author'] = 'anonymous'
        else:
            data['author'] = data['author']['username']
        return data

    class Meta:
        model = Message
        fields = ('author', 'pub_date', 'privacy', 'message_content')
        order_by = 'pub_date'
        depth = 2


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Simple user serializer
    """
    messages = serializers.HyperlinkedRelatedField(
            many=True,
            read_only=True,
            view_name='message-detail'
            )
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'messages')

