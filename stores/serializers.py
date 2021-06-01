from .models import Store, ReviewStore
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .services import create_subaccount

User = get_user_model()

class CreateStoreSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Store
        fields = ['id', 'name', 'owner', 'description', 'bank_name',  'account_number', 'twitter_handle', 'instagram_handle', 'country', 'slug', 'date_created']

        extra_kwargs = {
            "id":{
                "read_only": True
            },
            'date_created':{
                "read_only": True
            }
        }

    def create(self, validated_data):
        bank_name = validated_data['bank_name']
        account_number = str(validated_data['account_number'])
        print(account_number)
        response = create_subaccount(bank_name, f'0{account_number}')
        print(response)
        if response['result']['status'] == 'success':
            store = Store.objects.create(**validated_data)
        else:
            return {"error": "Sorry, your store cannot be created at the moment, try again later"}
        return store

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.twitter_handle = validated_data.get('twitter_handle', instance.twitter_handle)
        instance.instagram_handle = validated_data.get('instagram_handle', instance.instagram_handle)
        instance.save()
        return instance


class ListStoreSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['number_of_items'] = instance.store.count()
        representation['number_of_reviews'] = ReviewStore.objects.filter(store=instance).count()
        return representation
    class Meta:
        model = Store
        fields = ['id', 'name', 'owner', 'description', 'twitter_handle', 'instagram_handle', 'slug', 'date_created']

        extra_kwargs = {
            "id":{
                "read_only": True
            },

            "date_created":{
                "read_only": True
            }
        }

        

class ReviewStoreSerializer(serializers.ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ReviewStore

        fields = ['id', 'name', 'email', 'review', 'store', 'rating']

        extra_kwargs = {
            "id":{
                "read_only": True
            }
        }
