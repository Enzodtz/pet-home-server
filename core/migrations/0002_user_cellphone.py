# Generated by Django 4.0.1 on 2022-02-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cellphone',
            field=models.CharField(default='11989245633', max_length=11),
            preserve_default=False,
        ),
    ]