# Generated by Django 4.2.15 on 2024-09-03 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ('-date_created',)},
        ),
    ]
