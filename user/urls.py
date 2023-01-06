from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user import views

admin_user_router = DefaultRouter()
admin_user_router.register('', views.UsrInfoViewSet)

urlpatterns = [
    # user_info Router
    path('', include(admin_user_router.urls))
]
