# Generated by Django 4.0.2 on 2022-02-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_url',
            field=models.SlugField(default='#'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(upload_to='static/post_images'),
        ),
    ]
