# Generated by Django 3.2.16 on 2023-03-02 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_follow_unique_follow'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='post',
            name='unique_text_author',
        ),
    ]
