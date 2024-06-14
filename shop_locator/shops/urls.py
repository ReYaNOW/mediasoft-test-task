from django.urls import path

from shop_locator.shops import views

urlpatterns = [
    path('city/', views.CityListCreateView.as_view()),
    path('street/', views.StreetListCreateView.as_view()),
    path(
        'city/<int:city_id>/street/',
        views.StreetInCityListView.as_view(),
        name='street-in-city-list',
    ),
    path('shop/', views.ShopListCreateView.as_view()),
]
