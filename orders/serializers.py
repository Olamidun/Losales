from stores.models import Store
from items.models import Item
from .models import BillingAddress, Order, OrderItem
from rest_framework import serializers


class CreateOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())
    order_item = serializers.ListField(child=serializers.DictField(), write_only=True)
    email = serializers.EmailField()
    full_name =  serializers.CharField()
    address = serializers.CharField()
    total_cost = serializers.DecimalField(read_only=True, decimal_places=3, max_digits=12)
    # date_created = serializers.DateTimeField()



    # class Meta:
    #     model = Order

    #     fields = ['id', 'store', 'total_cost', 'full_name', 'email', 'address']

    #     extra_kwargs = {
    #         "id":{
    #             "read_only": True
    #         },
    #         "time_created": {
    #             "read_only": True
    #         }
    #     }

    def create(self, validated_data):
        address = validated_data.get('address')
        email = validated_data.get('email')
        store = validated_data.get('store')
        full_name = validated_data.get('full_name')
        order = Order.objects.create(
            full_name = full_name,
            address=address,
            email=email,
            store=store
        )

        item = validated_data.get('order_item')
        print(item)
        order_item_serializer = CreateOrderItemSerializer(data=item, many=True)
        order_item_serializer.is_valid(raise_exception=True)
        order_item_serializer.save(order_id=order.id)

        order.total_cost = 5000
        order.save()
        return order



class CreateOrderItemSerializer(serializers.Serializer):
    item_id = serializers.IntegerField(write_only=True)
    item = serializers.PrimaryKeyRelatedField(read_only=True)
    quantity = serializers.IntegerField()
    order_id = serializers.IntegerField(write_only=True, required=False)
    order = serializers.PrimaryKeyRelatedField(read_only=True)
    
    def create(self, validated_data):
        order = Order.objects.get(id=validated_data.get('order_id'))
        item = Item.objects.get(id=validated_data.get('item_id'))
        quantity = validated_data.get('quantity')
        price = float(quantity) * float(item.price)
        # delivery_fee = 0.075 * price
        return OrderItem.objects.create(
			items=item, order=order,
			quantity=quantity, total_cost=price
		)

    # order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    # items = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), many=True)

    # class Meta:
    #     model = OrderItem

    #     fields = ['id', 'items', 'order', 'quantity']

    #     extra_kwargs = {
    #         "id": {
    #             "read_only": True
    #         }
    #     }

    #     def create(self, validated_data):
    #         order_item =  OrderItem.objects.create(**validated_data)
    #         print(order_item)
    #         return order_item


'''
{
    "store": 1,
    "order_item": [
        {
            "item_id": 1,
            "quantity":2,
            "order_id":12
        },

        {
            "item_id": 9,
            "quantity":3,
            "order_id":12
        }
    ],
    "email": "kolapoolamidun@gmail.com",
    "full_name": "Kolapo Opeoluwa",
    "address": "56, ODK street"
}


'''