# Generated by Django 3.2.7 on 2021-09-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0021_rename_html_url_pullrequest_pr_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pullrequest',
            name='pr_link',
            field=models.URLField(verbose_name='PR Link'),
        ),
    ]
