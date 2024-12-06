# Generated by Django 5.1.2 on 2024-12-06 10:44

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_recipe_author_alter_review_user_delete_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
