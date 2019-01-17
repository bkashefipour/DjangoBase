# Generated by Django 2.1.4 on 2019-01-17 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0009_auto_20190117_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacilitySpace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('active', models.BooleanField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('capacity', models.PositiveSmallIntegerField(blank=True, default=1, null=True)),
                ('created_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='facilityspace_Creator', to=settings.AUTH_USER_MODEL)),
                ('facility', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.Facility')),
                ('modified_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='facilityspace_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('active', models.BooleanField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.Address')),
                ('created_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='household_Creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HouseholdMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('active', models.BooleanField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='householdmembership_Creator', to=settings.AUTH_USER_MODEL)),
                ('household', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.Household')),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.Person')),
                ('modified_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='householdmembership_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HouseholdMembershipType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('active', models.BooleanField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('isChild', models.BooleanField()),
                ('created_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='householdmembershiptype_Creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='householdmembershiptype_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('active', models.BooleanField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='teacher_Creator', to=settings.AUTH_USER_MODEL)),
                ('facility', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.Facility')),
                ('modified_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='teacher_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='householdmembership',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.HouseholdMembershipType'),
        ),
        migrations.AddField(
            model_name='household',
            name='member',
            field=models.ManyToManyField(through='base.HouseholdMembership', to='base.Person'),
        ),
        migrations.AddField(
            model_name='household',
            name='modified_by',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='household_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
