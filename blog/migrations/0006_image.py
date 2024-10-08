# Generated by Django 5.0.6 on 2024-07-14 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_reading_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='post_images/')),
                ('title', models.CharField(max_length=250, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.post', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصویر ها ',
                'ordering': ['created'],
                'indexes': [models.Index(fields=['created'], name='blog_image_created_1ba45b_idx')],
            },
        ),
    ]
