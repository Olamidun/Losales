from .models import Item
from django.contrib.auth import get_user_model
from rest_framework import serializers

# User = get_user_model()


class ItemSerializer(serializers.ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'store', 'discounted_price', ]

        extra_kwargs = {
            "id":{
                "read_only": True
            }
        }

        def create(self, validated_data):
            item = Item.objects.create(**validated_data)
            return item