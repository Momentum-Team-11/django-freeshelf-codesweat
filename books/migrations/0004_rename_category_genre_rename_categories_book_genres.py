# Generated by Django 4.0.3 on 2022-03-09 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_category_book_favorited_by_book_categories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Genre',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='categories',
            new_name='genres',
        ),
    ]
