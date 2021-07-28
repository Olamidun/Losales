from .models import Item
from stores.models import Store
from django.contrib.auth import get_user_model
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all(), required=False)
    class Meta:
        model = Item
        fields = ['id', 'name', 'item_image', 'price', 'store', 'discounted_price', 'out_of_stock']

        extra_kwargs = {
            "id":{
                "read_only": True
            }
        }
        def create(self, validated_data):
            item = Item.objects.create(**validated_data)
            return item

class ListItemSerializer(serializers.ModelSerializer):
    
    # def to_representation(self, instance):
    #     representation =  super().to_representation(instance)
    #     representation['images'] = ItemImageSerializer(ItemImage.objects.filter(item=instance), many=True).data
    #     return representation

    class Meta:
        model = Item
        fields = ['id', 'name', 'item_image', 'price', 'store', 'discounted_price', 'out_of_stock']
        depth = 1

        extra_kwargs = {
            "id":{
                "read_only": True
            }
        }

# class ItemImageSerializer(serializers.ModelSerializer):
#     item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), required=False)
#     class Meta:
#         model = ItemImage
#         fields = ['id', 'image', 'item']

#         extra_kwargs = {
#             "id":{
#                 "read_only": True
#             }
#         }

#         def create(self, validated_data):
#             image = validated_data['image']
#             item_image = ItemImage.objects.create(**validated_data)
#             return item_image
#             print(upload_data)