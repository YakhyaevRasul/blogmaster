from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework_simplejwt import views as jwt_views

from .views import *

app_name = 'posts'

urlpatterns  = [
    path('list/', PostListView.as_view(), name='post-list'),
    path('create/', PostCreateView.as_view(), name='create-post'),
    path('<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='detail-post'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

