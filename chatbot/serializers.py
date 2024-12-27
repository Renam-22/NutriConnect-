from rest_framework import serializers
from .models import ChatMessage

class ChatSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'