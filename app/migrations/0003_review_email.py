# Generated by Django 4.1.4 on 2023-12-20 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_listing_review_listings'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
