# Generated by Django 3.2.7 on 2021-09-13 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20210913_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='course',
            field=models.PositiveSmallIntegerField(choices=[(1, 'BTech'), (2, 'MCA')], default=1, verbose_name='Course'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='current_year',
            field=models.PositiveSmallIntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth')], default=1, verbose_name='Current Year'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='registration_no',
            field=models.CharField(default='NA', max_length=10, verbose_name='Registration Number'),
        ),
    ]
