# Generated by Django 5.1.2 on 2024-12-14 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='static/profile_pictures/image.png', null=True, upload_to='static/profile_pictures/'),
        ),
    ]
