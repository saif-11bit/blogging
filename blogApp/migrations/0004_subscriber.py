# Generated by Django 3.0.6 on 2020-06-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300)),
            ],
        ),
    ]