# Generated by Django 5.1.1 on 2024-12-26 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='bmi',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='goal',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
