from .models import *
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class AllRecipes(ListView):
    model = Recipe
    template_name = "main/all_recipes.html"

class AllBlogPosts(ListView):
    model = BlogPost
    template_name = "main/all_blog_posts.html"

class RecipeDetail(DetailView):
    model = Recipe
    template_name = "main/recipe_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.recipe = Recipe.objects.get(pk=self.kwargs["pk"])
        context["reviews"] = Review.objects.filter(recipe=self.recipe)
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