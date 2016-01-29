from rest_framework import serializers
from .models import Message, Thread
from django.contrib.auth.models import User

class ThreadSerializer(serializers.ModelSerializer):
    #participants = serializers.HyperlinkedRelatedField(view_name='participants', read_only=True, many=True)
    class Meta:
        model = Thread
        fields = ('id', 'url', 'name', 'participants', 'last_message')

    #def create(self, validated_data):
    #    return Thread.objects.create(**validated_data)


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'last_name', 'first_name')


