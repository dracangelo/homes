# Generated by Django 2.1.5 on 2020-05-06 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('title', models.CharField(max_length=70)),
                ('image', models.ImageField(upload_to='agents/')),
            ],
        ),
    ]
