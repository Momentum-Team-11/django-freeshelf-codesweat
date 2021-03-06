# Generated by Django 4.0.3 on 2022-03-09 21:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('slug', models.SlugField(blank=True, max_length=75, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='favorited_by',
            field=models.ManyToManyField(related_name='favorite_book', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(related_name='book', to='books.category'),
        ),
    ]
