# Generated by Django 5.0 on 2024-03-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobBazzar', '0006_remove_profile_id_alter_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='experience_field',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
