# Generated by Django 4.2.5 on 2024-02-01 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyxel', '0006_question_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='question_images/'),
        ),
    ]
