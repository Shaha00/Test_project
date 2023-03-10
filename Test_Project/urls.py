"""Test_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/', views.test),
    path('api/v1/products/', views.ProductListCreateAPIView.as_view()),
    path('api/v1/products/<int:id>/', views.product_detail_view),
    path('api/v1/profiles/', include('profiles.urls')),
    path('api/v1/categories/', views.CategoryListAPIView.as_view()),
    path('api/v1/tags/', views.TagModelViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('api/v1/tags/<int:id>', views.TagModelViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('api/v1/categories/<int:id>/', views.CategoryDetailAPIView.as_view())
]
