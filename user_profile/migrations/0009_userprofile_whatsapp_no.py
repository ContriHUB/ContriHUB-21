# Generated by Django 3.2.7 on 2021-10-14 09:44

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0008_alter_userprofile_registration_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='whatsapp_no',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None, verbose_name='Whatsapp Number'),
        ),
    ]
