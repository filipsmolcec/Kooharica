from main.forms import BlogPostForm, RecipeForm
from .models import *
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse

class AllRecipes(ListView):
    model = Recipe
    template_name = "main/recipe_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

class BestRecipes(ListView):
    template_name = "main/recipe_list.html"
    
    def get_queryset(self):
        avg_ratings = Recipe.objects.annotate(avg_rating=Avg('review__rating'))
        top_recipies = avg_ratings.order_by('-avg_rating')

        query = self.request.GET.get("q")
        if query:
            top_recipies = top_recipies.filter(title__icontains=query)[:20]
        else:
            top_recipies = top_recipies[:20]
        
        for recipe in top_recipies:
            if recipe.avg_rating is not None:
                recipe.avg_rating = round(recipe.avg_rating, 2)
        
        return top_recipies

class AllBlogPosts(ListView):
    model = BlogPost
    template_name = "main/blog_post_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

class RecipeDetail(DetailView):
    model = Recipe
    template_name = "main/recipe_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.recipe = Recipe.objects.get(pk=self.kwargs["pk"])
        context["reviews"] = Review.objects.filter(recipe=self.recipe)
        average_rating = context["reviews"].aggregate(avg_rating=Avg('rating'))['avg_rating']
        context["avg_rating"] = round(average_rating, 2) if average_rating is not None else 5
        return context

class BlogDetail(DetailView):
    model = BlogPost
    template_name = "main/blog_detail.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class UserDetail(DetailView):
    model = User
    template_name = "main/user_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["recipes"] = Recipe.objects.filter(author=self.kwargs["pk"])
        return context

def index(request):
    return render(request, "main/index.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def recipe_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.date_posted = timezone.now()
            entry.date_updated = timezone.now()
            entry.save()
            return redirect('recipe_detail', pk=entry.pk)
    else:
        form = RecipeForm()

    context = {'form': form}
    return render(request, 'main/form.html', context)

def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.date_posted = timezone.now()
            entry.date_updated = timezone.now()
            entry.save()
            return redirect('recipe_detail', pk=entry.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'main/form.html', {'form': form})

def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')
    return render(request, 'main/confirm_delete.html', {'object': recipe, 'redirect': reverse('recipes')})

def blog_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST)

        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.date_posted = timezone.now()
            entry.date_updated = timezone.now()
            entry.save()
            return redirect('blog_detail', pk=entry.pk)
    else:
        form = BlogPostForm()

    context = {'form': form}
    return render(request, 'main/form.html', context)

def blog_update(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.date_posted = timezone.now()
            entry.date_updated = timezone.now()
            entry.save()
            return redirect('blog_detail', pk=entry.pk)
    else:
        form = BlogPostForm(instance=blog)
    return render(request, 'main/form.html', {'form': form})

def blog_delete(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_posts')
    return render(request, 'main/confirm_delete.html', {'object': blog, 'redirect': reverse('blog_posts')})