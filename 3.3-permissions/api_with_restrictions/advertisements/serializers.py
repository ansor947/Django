from django.contrib.auth.models import User
from django.forms import ValidationError
from rest_framework import serializers
from advertisements.models import Advertisement
from api_with_restrictions.advertisements.models import AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)
        read_only_fields = ['creator']


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(read_only=True,)

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'description', 'creator', 'status', 'created_at']

    def create(self, validated_data):
        """Метод для создания"""

        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate_status(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        if self.context['request'].method == 'POST' or self.context['request'].method == 'PATCH':

            count= Advertisement.objects.filter(status=AdvertisementStatusChoices.OPEN).count()

            if count>= 10:
                raise serializers.ValidationError()
            return data
        




