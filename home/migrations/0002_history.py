# Generated by Django 3.0.5 on 2020-07-16 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
