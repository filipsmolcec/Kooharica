from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('recepti/', views.AllRecipes.as_view(), name='recipes'),
    path('recepti/<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('recepti/izradi/', views.recipe_create, name='recipe_create'),
    path('recepti/<int:pk>/update/', views.recipe_update, name='recipe_update'),
    path('recepti/<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
    path('recepti/najbolji/', views.BestRecipes.as_view(), name='best_recipes'),  

    path('blogovi/', views.AllBlogPosts.as_view(), name='blog_posts'),
    path('blogovi/<int:pk>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('blogovi/izradi', views.blog_create, name='blog_create'),
    path('blogovi/<int:pk>/update/', views.blog_update, name='blog_update'),
    path('blogovi/<int:pk>/delete/', views.blog_delete, name='blog_delete'),

    path('korisnici/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('accounts/register/', views.register, name='register'),
]