from rest_framework import serializers

from .models import Edge

class EdgeSerializer(serializers.ModelSerializer):
    user1 = serializers.CharField(source='user1.username', read_only=True)
    user2 = serializers.CharField(source='user2.username', read_only=True)
    class Meta:
        model = Edge
        fields = ('pk', 'user1', 'user2', 'weight')
