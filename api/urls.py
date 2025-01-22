from django.urls import path
from api import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('recipes/', views.RecipeList.as_view()),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view()),

    path('blogs/', views.BlogPostList.as_view()),
    path('blogs/<int:pk>/', views.BlogPostDetail.as_view()),
]