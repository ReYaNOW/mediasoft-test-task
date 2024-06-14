from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect

from shop_locator.shops.models import City, Street, Shop
from shop_locator.utils import fill_db_cities_streets


def redirect_to_docs(request):
    response = redirect('/docs')
    return response


class FillDbCitiesStreets(APIView):
    def post(self, request):
        if City.objects.exists():
            return Response(
                {
                    'status': 'failed',
                    'log': 'Please clear db before filling it',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        fill_db_cities_streets(City, Street)
        return Response({'status': 'success'}, status=status.HTTP_200_OK)


class ClearDb(APIView):
    def delete(self, request):
        Shop.objects.all().delete()
        Street.objects.all().delete()
        City.objects.all().delete()
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
