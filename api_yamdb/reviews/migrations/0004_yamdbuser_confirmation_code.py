# Generated by Django 3.2 on 2023-02-19 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_remove_yamdbuser_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='yamdbuser',
            name='confirmation_code',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='Код подтвержедния'),
        ),
    ]
