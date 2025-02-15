from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "name", "url", "time", "place", "interest_sports", "interest_arts", "interest_social", "interest_env", "interest_drinks", "interest_startups", "interest_games", "interest_photography"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }

    def create(self, validated_data):
        return User.objects.create(**validated_data)
        # password = validated_data.pop("password")
        # user = User(**validated_data)
        # user.set_password(password)
        # user.save()
        # return user
