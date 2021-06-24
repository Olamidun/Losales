from .models import Store, ReviewStore
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .services import SubaccountClass, BadRequestToFlutterwave
import os
from dotenv import load_dotenv

load_dotenv()

User = get_user_model()
subaccount = SubaccountClass(os.getenv('secret_key'))

class CreateStoreSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Store
        fields = ['id', 'name', 'owner', 'description', 'store_image', 'bank_name',  'account_number', 'twitter_handle', 'instagram_handle', 'country', 'slug', 'date_created']

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
        business_name = validated_data['name']
        print(account_number)
        response = subaccount.create_subaccount(bank_name, f'0{account_number}', business_name)
        print(response)
        if response['result']['status'] == 'success':
            store = Store.objects.create(**validated_data)
            store.subaccount_id = response['result']['data']['subaccount_id']
            store.s_id = response['result']['data']['id']
            store.save()
        else:
            raise BadRequestToFlutterwave()
        return store

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.twitter_handle = validated_data.get('twitter_handle', instance.twitter_handle)
        instance.instagram_handle = validated_data.get('instagram_handle', instance.instagram_handle)
        subaccount.update_subaccount(instance.s_id, instance.name)
        instance.save()
        return instance


class ListStoreSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        subaccount_transaction = subaccount.fetch_subaccount(instance.s_id)
        representation = super().to_representation(instance)
        representation['number_of_items'] = instance.store.count()
        representation['number_of_reviews'] = ReviewStore.objects.filter(store=instance).count()
        representation['subaccount_earnings'] = subaccount_transaction['data']
        return representation
    class Meta:
        model = Store
        fields = ['id', 'name', 'owner', 'description', 'store_image', 'twitter_handle', 'instagram_handle', 'slug', 'date_created', 's_id', 'subaccount_id']

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
