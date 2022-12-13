from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [

    path('', views.api_overview),

    path('messages/', views.messages_handler),
    path('messages/<int:pk>/', views.message_handler),
    path('messages/unread/', views.unread_messages),


    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    ]

