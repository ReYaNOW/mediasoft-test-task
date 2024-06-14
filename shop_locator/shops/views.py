from django.db.models import Q
from django.utils.timezone import localtime
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from shop_locator.shops.models import City, Street, Shop
from shop_locator.shops.serializers import (
    CitySerializer,
    StreetSerializer,
    ShopSerializer,
    ShopCreateSerializer,
    ShopQuerySerializer,
)
from shop_locator.utils import PROPERTIES


class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetListCreateView(generics.ListCreateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class StreetInCityListView(generics.ListAPIView):
    serializer_class = StreetSerializer

    def get_queryset(self):
        city_id = self.kwargs['city_id']
        return Street.objects.filter(city_id=city_id)


class ShopListCreateView(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ShopSerializer
        else:
            return ShopCreateSerializer

    @swagger_auto_schema(
        query_serializer=ShopQuerySerializer(),
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # spent six hours to find how to make default value a time, not 'string'
    # in opening_time and closing_time fields
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT, properties=PROPERTIES
        )
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Shop.objects.all()
        query_params = self.request.query_params

        street_name = query_params.get('street')
        if street_name:
            queryset = queryset.filter(street__name=street_name)

        city_name = query_params.get('city')
        if city_name:
            queryset = queryset.filter(city__name=city_name)

        open_boolean = query_params.get('open')
        if open_boolean:
            # using localtime to ease testing of this app
            current_time = localtime().time()
            if open_boolean == '1':
                queryset = queryset.filter(
                    Q(
                        opening_time__lte=current_time,
                        closing_time__gt=current_time,
                    )
                )
            else:
                queryset = queryset.filter(
                    ~Q(
                        opening_time__lte=current_time,
                        closing_time__gt=current_time,
                    )
                )

        return queryset
