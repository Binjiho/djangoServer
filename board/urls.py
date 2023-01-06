from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

admin_board_router = DefaultRouter()
admin_board_router.register(r'user_board', views.UserBoardViewSet)

urlpatterns = [
    # site_evt URL
    path('site_evt/', views.getData),
    path('site_evt/detail/<int:evt_no>', views.detail),

    # user_board URL
    # path('user_board/', views.user_board_list),
    # path('user_board/<int:pk>/', views.user_board_detail),

    # user_board Router
    path('', include(admin_board_router.urls))

]
