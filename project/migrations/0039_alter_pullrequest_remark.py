# Generated by Django 3.2.7 on 2021-10-13 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0038_alter_pullrequest_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pullrequest',
            name='remark',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
