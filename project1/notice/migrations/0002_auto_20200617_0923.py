# Generated by Django 3.0.7 on 2020-06-17 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='contents',
            field=models.TextField(null=True),
        ),
    ]
