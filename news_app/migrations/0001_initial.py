# Generated by Django 4.1 on 2023-04-12 03:24

from django.db import migrations, models
import news_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date', models.CharField(max_length=12)),
                ('author', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=news_app.models.upload_image)),
                ('source', models.CharField(max_length=100)),
            ],
        ),
    ]
