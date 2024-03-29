# Generated by Django 3.1.2 on 2020-10-12 17:49

from django.db import migrations, models
import shorts.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.TextField(verbose_name='Original Url')),
                ('key', models.CharField(default=shorts.utils.generate_random_key, max_length=50, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
