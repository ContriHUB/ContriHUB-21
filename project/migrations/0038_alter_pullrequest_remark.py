# Generated by Django 3.2.7 on 2021-10-13 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0037_pullrequest_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pullrequest',
            name='remark',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
