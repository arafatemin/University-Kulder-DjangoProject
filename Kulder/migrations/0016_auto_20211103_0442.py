# Generated by Django 3.2.8 on 2021-11-03 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kulder', '0015_auto_20211103_0410'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='comments',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]