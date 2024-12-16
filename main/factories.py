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
    content = factory.Faker("paragraph", nb_sentences=30)
    author = factory.LazyFunction(lambda: User.objects.order_by("?").first() or UserFactory())
    date_posted = factory.Faker("date")
    date_updated = factory.Faker("date")

class RecipeFactory(DjangoModelFactory):
    class Meta:
        model = Recipe

    title = factory.Faker("sentence", nb_words=6)
    instructions = factory.Faker("paragraph", nb_sentences=16)
    cook_time_minutes = factory.LazyFunction(lambda: random.randint(5, 120))
    author = factory.LazyFunction(lambda: User.objects.order_by("?").first() or UserFactory())
    date_posted = factory.Faker("date_time_this_year")
    date_updated = factory.LazyAttribute(lambda obj: obj.date_posted)

class ReviewFactory(DjangoModelFactory):
    class Meta:
        model = Review

    recipe = factory.LazyFunction(lambda: Recipe.objects.order_by("?").first() or RecipeFactory())
    author = factory.LazyFunction(lambda: User.objects.order_by("?").first() or UserFactory())
    rating = factory.LazyFunction(lambda: random.randint(1, 5))
    comment = factory.Faker("paragraph", nb_sentences=3)
    date_posted = factory.Faker("date")