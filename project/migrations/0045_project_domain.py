# Generated by Django 3.2.7 on 2021-10-19 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0044_remove_project_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='domain',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project.domain'),
        ),
    ]
