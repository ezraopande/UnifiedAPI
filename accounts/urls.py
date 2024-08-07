from django.urls import path
from . import views
from knox.views import LogoutView, LogoutAllView
from .views import UserListView, UserDetailView


urlpatterns = [
    path('register/', views.CreateUserAPI.as_view()),
    path('update-user/<int:pk>/', views.UpdateUserAPI.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view()),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail')
]
