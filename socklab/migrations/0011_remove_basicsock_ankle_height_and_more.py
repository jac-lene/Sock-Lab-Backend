# Generated by Django 4.0.6 on 2022-07-14 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socklab', '0010_remove_basicsock_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicsock',
            name='ankle_height',
        ),
        migrations.RemoveField(
            model_name='basicsock',
            name='foot_length',
        ),
        migrations.AddField(
            model_name='basicsock',
            name='status',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]