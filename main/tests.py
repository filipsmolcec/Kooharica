from django.test import TestCase
from django.urls import reverse
from main.models import Recipe, BlogPost, Review
from django.contrib.auth.models import User

class TestModels(TestCase):
    def test_recipe_create(self):
        test_user = User.objects.create_user(username="testuser", password="testpassword")
        recipe = Recipe.objects.create(
            author=test_user,
            title="Test Recipe",
            instructions="This is a test recipe",
            cook_time_minutes=30
        )
        self.assertEqual(recipe.title, "Test Recipe")
        self.assertEqual(recipe.instructions, "This is a test recipe")
        self.assertEqual(recipe.cook_time_minutes, 30)

    def test_blog_create(self):
        test_user = User.objects.create_user(username="testuser", password="testpassword")
        blog = BlogPost.objects.create(
            author=test_user,
            title="Test Blog",
            content="This is a test blog",
        )
        self.assertEqual(blog.title, "Test Blog")
        self.assertEqual(blog.content, "This is a test blog")

    def test_review_create(self):
        test_user = User.objects.create_user(username="testuser", password="testpassword")
        test_recipe = Recipe.objects.create(
            author=test_user,
            title="Test Recipe",
            instructions="This is a test recipe",
            cook_time_minutes=30
        )
        review = Review.objects.create(
            recipe=test_recipe,
            author=test_user,
            rating=5,
            comment="This is a test review"
        )
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, "This is a test review")

class TestViews(TestCase):
    def test_get_home(self):
        url = reverse("index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/index.html")

    def test_get_recipe_list(self):
        url = reverse("recipes")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/recipe_list.html")
    
    def test_get_blog_list(self):
        url = reverse("blog_posts")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/blog_post_list.html")

    def test_post_recipe(self):
        User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        url = reverse("recipe_create")
        response = self.client.post(url, {
            "title": "Test Recipe",
            "instructions": "This is a test recipe",
            "cook_time_minutes": 30
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Recipe.objects.count(), 1)

    def test_post_review(self):
        User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        test_user = User.objects.get(username="testuser")
        test_recipe = Recipe.objects.create(
            author=test_user,
            title="Test Recipe",
            instructions="This is a test recipe",
            cook_time_minutes=30
        )
        url = reverse("recipe_detail", args=[test_recipe.pk])
        response = self.client.post(url, {
            "rating": 5,
            "comment": "This is a test review"
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 1)

    def test_post_blog(self):
        User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        url = reverse("blog_create")
        response = self.client.post(url, {
            "title": "Test Blog",
            "content": "This is a test blog"
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.count(), 1)