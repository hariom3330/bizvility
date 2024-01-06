# Generated by Django 4.1.4 on 2024-01-04 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_review_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='review',
            name='listings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.listing'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
    ]