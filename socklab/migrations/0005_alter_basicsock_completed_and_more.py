# Generated by Django 4.0.6 on 2022-07-08 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socklab', '0004_basicsock_completed_basicsock_foot_stripe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicsock',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basicsock',
            name='foot_stripe',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basicsock',
            name='in_progress',
            field=models.BooleanField(default=False),
        ),
    ]
