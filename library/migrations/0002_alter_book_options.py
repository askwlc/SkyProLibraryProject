# Generated by Django 5.1 on 2024-09-04 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title'], 'permissions': [('can_review_book', 'Can review book'), ('can_recommend_book', 'Can recommend book')], 'verbose_name': 'книга', 'verbose_name_plural': 'книги'},
        ),
    ]