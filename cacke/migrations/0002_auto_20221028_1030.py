# Generated by Django 3.2.15 on 2022-10-28 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cacke', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulka',
            name='Nachinka',
        ),
        migrations.AddField(
            model_name='bulka',
            name='nachinka',
            field=models.TextField(default='simple'),
        ),
        migrations.AddField(
            model_name='bulka',
            name='price',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='bulka',
            name='testo',
            field=models.TextField(default='simple'),
        ),
    ]
