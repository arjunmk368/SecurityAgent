# Generated by Django 3.0.2 on 2020-01-10 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_the_User', models.TextField(blank='True', default='False', max_length='512', null='True')),
                ('Age', models.IntegerField(blank='True', default='False', null='True')),
                ('Allowed', models.BooleanField(default=True)),
            ],
        ),
    ]
