from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factories import *

USERS_COUNT = 1
BLOG_POSTS_COUNT = 100
RECIPIES_COUNT = 100
REVIEWS_COUNT = 5000

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        
        #models = [Review]
        #for m in models:
        #    m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(USERS_COUNT):
            user = UserFactory()

        for _ in range(BLOG_POSTS_COUNT):
            blog = BlogPostFactory()

        for _ in range(RECIPIES_COUNT):
            recipe = RecipeFactory()
        
        for _ in range(REVIEWS_COUNT):
            review = ReviewFactory()