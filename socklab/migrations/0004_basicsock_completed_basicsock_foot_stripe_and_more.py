# Generated by Django 4.0.6 on 2022-07-08 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socklab', '0003_alter_basicsock_cc2_alter_basicsock_cc3'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicsock',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='basicsock',
            name='foot_stripe',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='basicsock',
            name='in_progress',
            field=models.BooleanField(default=False),
        ),
    ]
