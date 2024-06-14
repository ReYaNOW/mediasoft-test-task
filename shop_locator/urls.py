"""
URL configuration for shop_locator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from shop_locator import views

schema_view = get_schema_view(
    openapi.Info(
        title='Shop API docs',
        default_version='v1',
        description='Documentation for api, '
                    'where you can make requests via ui.',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', include('shop_locator.shops.urls')),
    path('utility/fill_db', views.FillDbCitiesStreets.as_view()),
    path('utility/clear_db', views.ClearDb.as_view()),
    path(
        'docs/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path('', views.redirect_to_docs),
    path('admin/', admin.site.urls),
]
