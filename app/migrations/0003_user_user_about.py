# Generated by Django 5.1.3 on 2024-11-27 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_post_picture_id_alter_post_post_parent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_about',
            field=models.TextField(blank=True, max_length=190, null=True),
        ),
    ]