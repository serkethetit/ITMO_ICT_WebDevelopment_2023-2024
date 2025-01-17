# Generated by Django 4.2.6 on 2023-10-29 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tour_project", "0002_country_alter_review_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="tour",
            name="is_sold",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="review",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
