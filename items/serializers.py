from .models import Item
from stores.models import Store
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

# User = get_user_model()


class ItemSerializer(serializers.ModelSerializer):
    # def get_logged_in_user(self):
    #     user = None
    #     request = self.context.get("request")
    #     if request and hasattr(request, "user"):
    #         return request.user.id
        # return None

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