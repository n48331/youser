# Generated by Django 3.1 on 2022-03-29 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220325_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='pics/default_post.jpg', upload_to='pics/docs/'),
        ),
    ]
