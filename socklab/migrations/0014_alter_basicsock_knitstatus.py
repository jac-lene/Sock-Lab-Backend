# Generated by Django 4.0.6 on 2022-07-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socklab', '0013_rename_knitstatus_basicsock_knitstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicsock',
            name='knitStatus',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
