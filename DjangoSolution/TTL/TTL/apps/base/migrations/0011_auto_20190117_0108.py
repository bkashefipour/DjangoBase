# Generated by Django 2.1.4 on 2019-01-17 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20190117_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='household',
            name='address',
        ),
        migrations.RemoveField(
            model_name='household',
            name='id',
        ),
        migrations.RemoveField(
            model_name='household',
            name='member',
        ),
        migrations.AddField(
            model_name='household',
            name='consumer',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='base.Consumer'),
            preserve_default=False,
        ),
    ]
