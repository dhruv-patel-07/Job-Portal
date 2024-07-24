# Generated by Django 5.0 on 2024-03-22 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobBazzar', '0016_job_zipcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('applicant_email', models.EmailField(max_length=254)),
                ('company_email', models.EmailField(max_length=254)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(default='applied', max_length=40)),
                ('job_id', models.CharField(max_length=30)),
                ('interview', models.CharField(max_length=40)),
                ('job_title', models.CharField(max_length=80)),
                ('cv', models.ImageField(upload_to='CV/')),
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.CharField(editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]