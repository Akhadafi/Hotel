# Generated by Django 3.2.13 on 2022-05-25 15:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_auto_20220525_0011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', 'created']},
        ),
        migrations.AddField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
