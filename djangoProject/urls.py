from django.contrib import admin
from django.urls import path, include
from .views import Main
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from user.urls import admin_user_router
from board.urls import admin_board_router
from product.urls import admin_product_router


admin_api_urls = [
    path("user/", include((admin_user_router.urls, 'user'))),
    path('board/', include((admin_board_router.urls, 'board.urls'))),
    path('product/', include((admin_product_router.urls, 'product.urls'))),
]

api_urls = [
    path("admin/", include((admin_api_urls, 'admin'))),
]


urlpatterns = [
    path("admin/", include((admin_api_urls, 'admin'))),
    # path('admin/', admin.site.urls),
    # path('user/', include('user.urls')),
    path('', Main.as_view()),
    # path('board/', include('board.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
