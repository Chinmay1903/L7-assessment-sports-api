"""
URL configuration for sports_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Schema view for Swagger and ReDoc UI
schema_view = get_schema_view(
   openapi.Info(
      title="SportsApp API",
      default_version='v1',
      description="API documentation for the Sports Application",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@sportsapp.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # URL pattern for the Django admin interface
    path('admin/', admin.site.urls),
    
    # URL pattern for the sports app API endpoints
    path('api/', include('sportsapp.urls')),

    # URL pattern for the Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # URL pattern for the ReDoc UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
