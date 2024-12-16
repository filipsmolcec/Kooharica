from django.db import transaction
from django.core.management.base import BaseCommand
from main.models import *
from main.factories import *

USERS_COUNT = 100
BLOG_POSTS_COUNT = 100
RECIPIES_COUNT = 100
REVIEWS_COUNT = 5000

class Command(BaseCommand):
    help = "Delete all test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting data...")
        
        for acc in User.objects.all():
            if acc.is_staff:
                continue
            acc.delete()

        models = [BlogPost, Recipe, Review]
        for m in models:
            m.objects.all().delete()
