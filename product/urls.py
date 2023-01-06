from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product import views

admin_product_router = DefaultRouter()
admin_product_router.register('', views.GoodsViewSet)

urlpatterns = [
    # user_info Router
    path('', include(admin_product_router.urls))
]
