# Generated by Django 5.0 on 2024-04-08 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0003_alter_subscribe_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscribe',
            old_name='email',
            new_name='sub_email',
        ),
    ]