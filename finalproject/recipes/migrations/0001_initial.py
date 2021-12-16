# Generated by Django 2.2 on 2021-12-14 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_author', models.CharField(max_length=500)),
                ('item_ingredients', models.CharField(max_length=20000)),
                ('item_instructions', models.CharField(max_length=50000)),
                ('item_description', models.CharField(max_length=50000)),
                ('item_rating', models.IntegerField()),
            ],
        ),
    ]