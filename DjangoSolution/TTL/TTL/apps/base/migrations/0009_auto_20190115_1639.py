# Generated by Django 2.1.4 on 2019-01-16 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20190115_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='member',
            field=models.ManyToManyField(through='base.HouseholdMembership', to='base.Person'),
        ),
        migrations.AlterField(
            model_name='householdmembership',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.HouseholdMembershipType'),
        ),
    ]
