from rest_framework.viewsets import ModelViewSet
from tapmenuapp.models import (
    Restaurant,
    RestaurantImage,
    RestaurantAddress,
    RestaurantMenuImage,
    Category,
    Item,
    ItemImage,
)
from tapmenuapp.serializers import (
    RestaurantSerializer,
    RestaurantImageSerializer,
    RestaurantImageWithRestaurantSerializer,
    RestaurantAddressSerializer,
    RestaurantAddressWithRestaurantSerializer,
    RestaurantMenuImageSerializer,
    RestaurantMenuImageWithRestaurantSerializer,
    CategorySerializer,
    CategoryWithRestaurantSerializer,
    ItemSerializer,
    ItemWithCategorySerializer,
    ItemImageSerializer,
    ItemImageWithItemSerializer,
)


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantImageViewSet(ModelViewSet):
    queryset = RestaurantImage.objects.all()
    serializer_class = RestaurantImageSerializer

    def get_serializer_class(self):
        serializer_map = {
            'retrieve': RestaurantImageWithRestaurantSerializer,
        }
        return serializer_map.get(self.action, self.serializer_class)


class RestaurantAddressViewSet(ModelViewSet):
    queryset = RestaurantAddress.objects.all()
    serializer_class = RestaurantAddressSerializer

    def get_serializer_class(self):
        serializer_map = {
            'retrieve': RestaurantAddressWithRestaurantSerializer,
        }
        return serializer_map.get(self.action, self.serializer_class)


class RestaurantMenuImageViewSet(ModelViewSet):
    queryset = RestaurantMenuImage.objects.all()
    serializer_class = RestaurantMenuImageSerializer

    def get_serializer_class(self):
        serializer_map = {
            'retrieve': RestaurantMenuImageWithRestaurantSerializer,
        }
        return serializer_map.get(self.action, self.serializer_class)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        serializer_map = {
            'retrieve': CategoryWithRestaurantSerializer,
        }
        return serializer_map.get(self.action, self.serializer_class)


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_clsas = ItemSerializer

    def get_serializer_class(self):
        serializer_map = {
            'retrieve': ItemWithCategorySerializer,
        }
        return serializer_map.get(self.action, self.serializer_class)


class ItemImageViewSet(ModelViewSet):
    queryset = ItemImage.objects.all()
    serializer_class = ItemImageSerializer

    def get_serializer_class(self):
        serializer_map = {
            'retrieve': ItemImageWithItemSerializer,
        }
        return serializer_map.get(self.action, self.serializer_class)
