# Generated by Django 4.2.1 on 2023-05-23 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DamirsinbaChasti',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('url', models.CharField(max_length=250)),
                ('preview', models.CharField(max_length=250)),
            ],
        ),
    ]
