# Generated by Django 4.2.5 on 2023-09-08 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_campaign', '0003_alter_subscriber_status_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='status_tag',
            field=models.CharField(default='active', max_length=255),
        ),
    ]
