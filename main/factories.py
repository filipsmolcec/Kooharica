## factories.py
import factory
import random
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model

from main.models import *

User = get_user_model()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.Faker("password")

class BlogPostFactory(DjangoModelFactory):
    class Meta:
        model = BlogPost

    title = factory.Faker("sentence")
    content = factory.Faker("texts")
    author = User.objects.all()[random.randint(0, User.objects.all().count()-1)]
    date_posted = factory.Faker("date")
    date_updated = factory.Faker("date")

class RecipeFactory(DjangoModelFactory):
    class Meta:
        model = Recipe

    title = factory.Faker("sentence")
    instructions = factory.Faker("texts")
    cook_time_minutes = random.randint(5, 100)
    author = User.objects.all()[random.randint(0, User.objects.all().count()-1)]
    date_posted = factory.Faker("date")
    date_updated = factory.Faker("date")

class ReviewFactory(DjangoModelFactory):
    class Meta:
        model = Review

    recipe = Recipe.objects.all()[random.randint(0, Recipe.objects.all().count()-1)]
    author = User.objects.all()[random.randint(0, User.objects.all().count()-1)]
    rating = random.randint(1, 5)
    comment = factory.Faker("sentences")
    date_posted = factory.Faker("date")