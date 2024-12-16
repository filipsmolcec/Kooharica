from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factories import *

USERS_COUNT = 100
BLOG_POSTS_COUNT = 100
RECIPIES_COUNT = 100
REVIEWS_COUNT = 1000

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Creating new data...")

        users = UserFactory.create_batch(USERS_COUNT)
        recipies = RecipeFactory.create_batch(RECIPIES_COUNT)
        blogs = BlogPostFactory.create_batch(BLOG_POSTS_COUNT)
        reviews = ReviewFactory.create_batch(REVIEWS_COUNT)
