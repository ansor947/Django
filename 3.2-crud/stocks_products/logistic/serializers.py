from rest_framework import serializers

from stocks_products.logistic.models import Product, Stock


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'products']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'products', 'positions']

    # def create(self, validated_data):
    #     positions = validated_data.pop('positions')
    #     stock = super().create(validated_data)
    #     return stock

    # def update(self, instance, validated_data):
    #     positions = validated_data.pop('positions')
    #     stock = super().update(instance, validated_data)
    #     return stock
    
    def update_or_create(self, validated_data):
        positions = validated_data.pop('positions')
        address = validated_data.pop('address')
        values_for_update={"address": address, "positions": positions}
        id,stock = Stock.objects.update_or_create(id=1, defaults = values_for_update)
        return stock
