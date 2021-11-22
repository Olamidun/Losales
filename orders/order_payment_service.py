class OrderPaymentService:
    @staticmethod
    def calculate_commission_for_each_item_in_order(order_item):
        seller_commission = 0.95 * float(order_item.total_cost)

        losales_commission = float(order_item.total_cost) - seller_commission

        order_item.seller_commission = seller_commission
        order_item.losales_commission = losales_commission

        order_item.save()
        return order_item.seller_commission