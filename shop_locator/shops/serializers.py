from rest_framework import serializers

from shop_locator.shops.models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    street = serializers.SlugRelatedField(
        'name', queryset=Street.objects.all()
    )

    class Meta:
        model = Shop
        fields = [
            'id',
            'name',
            'city',
            'street',
            'house',
            'opening_time',
            'closing_time',
        ]


class ShopCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ShopQuerySerializer(serializers.Serializer):
    city = serializers.CharField(required=False)
    street = serializers.CharField(required=False)
    open = serializers.ChoiceField(choices=[0, 1], required=False)
