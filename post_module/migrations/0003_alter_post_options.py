# Generated by Django 4.0.2 on 2022-09-15 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_module', '0002_alter_post_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-slug']},
        ),
    ]
