# Generated by Django 4.0 on 2023-02-16 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=25),
        ),
    ]