# Generated by Django 5.0 on 2024-03-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobBazzar', '0007_profile_experience_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='experience_field',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
