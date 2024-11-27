from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
    
class Recipe(models.Model):
    title = models.CharField(max_length=50)
    instructions = models.TextField(blank=False, null=False)
    cook_time_minutes = models.IntegerField()
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    recipe = models.ForeignKey(Recipe, default=1, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return "{}Review{}".format(str(self.user), str(self.date_posted))
    
