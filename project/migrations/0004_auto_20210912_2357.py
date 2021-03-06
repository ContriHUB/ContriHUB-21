# Generated by Django 3.2.7 on 2021-09-12 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0003_assignedissue'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='assignee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assignee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issue',
            name='mentor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mentor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issue',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Open'), (2, 'Assigned'), (3, 'Closed')], default=1, verbose_name='State'),
        ),
        migrations.DeleteModel(
            name='AssignedIssue',
        ),
    ]
