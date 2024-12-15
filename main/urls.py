from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recepti/', views.AllRecipes.as_view()),
    path('blogovi/', views.AllBlogPosts.as_view()),
    path('accounts/register/', views.register, name='register')
]