# Generated by Django 3.0.6 on 2020-06-07 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0005_auto_20200607_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crousal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Crousal')),
            ],
        ),
    ]
