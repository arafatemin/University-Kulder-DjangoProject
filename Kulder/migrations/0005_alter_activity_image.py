# Generated by Django 3.2.8 on 2021-10-30 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kulder', '0004_alter_activity_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Activity/'),
        ),
    ]
