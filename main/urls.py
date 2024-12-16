from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recepti/', views.AllRecipes.as_view(), name='recipes'),
    path('recepti/<pk>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('blogovi/', views.AllBlogPosts.as_view(), name='blog_posts'),
    path('blogovi/<pk>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('korisnici/<pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('accounts/register/', views.register, name='register')
]