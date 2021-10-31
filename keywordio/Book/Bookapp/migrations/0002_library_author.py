# Generated by Django 3.2.7 on 2021-10-30 15:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]