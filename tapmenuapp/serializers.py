from tapmenuapp.models import (
    Restaurant,
    RestaurantImage,
    RestaurantAddress,
    RestaurantMenuImage,
    Category,
    Item,
    ItemImage,
)
from rest_framework.serializers import ModelSerializer


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class RestaurantImageSerializer(ModelSerializer):
    class Meta:
        model = RestaurantImage
        fields = '__all__'


class RestaurantImageWithRestaurantSerializer(ModelSerializer):
    restaurant = RestaurantSerializer()

    class Meta:
        model = RestaurantImage
        fields = '__all__'


class RestaurantAddressSerializer(ModelSerializer):
    class Meta:
        model = RestaurantAddress
        fields = '__all__'


class RestaurantAddressWithRestaurantSerializer(ModelSerializer):
    restaurant = RestaurantSerializer()

    class Meta:
        model = RestaurantAddress
        fields = '__all__'


class RestaurantMenuImageSerializer(ModelSerializer):
    class Meta:
        model = RestaurantMenuImage
        fields = '__all__'


class RestaurantMenuImageWithRestaurantSerializer(ModelSerializer):
    restaurant = RestaurantSerializer()

    class Meta:
        model = RestaurantMenuImage
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryWithRestaurantSerializer(ModelSerializer):
    restaurant = RestaurantSerializer()

    class Meta:
        model = Category
        fields = '__all__'


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemWithCategorySerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Item
        fields = '__all__'


class ItemImageSerializer(ModelSerializer):
    class Meta:
        model = ItemImage
        fields = '__all__'


class ItemImageWithItemSerializer(ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = ItemImage
        fields = '__all__'
