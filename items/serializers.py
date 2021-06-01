from .models import Item, ItemImage
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


class ItemImageSerializer(serializers.ModelSerializer):
    # item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    class Meta:
        model = ItemImage
        fields = ['id', 'image', 'item']

        extra_kwargs = {
            "id":{
                "read_only": True
            }
        }

        def create(self, validated_data):
            item_image = ItemImage.objects.create(**validated_data)
            return item_image