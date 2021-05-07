from .models import Item
from stores.models import Store
from django.contrib.auth import get_user_model
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())
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