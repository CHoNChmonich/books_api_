# Generated by Django 5.1.4 on 2024-12-08 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
