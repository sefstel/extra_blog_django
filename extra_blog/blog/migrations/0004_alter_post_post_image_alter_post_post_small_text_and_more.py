# Generated by Django 4.0.2 on 2022-02-08 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_post_text_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(upload_to='post_files'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_small_text',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]
