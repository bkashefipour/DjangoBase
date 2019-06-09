# Generated by Django 2.1.4 on 2019-06-09 02:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('active', models.BooleanField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('street_line1', models.CharField(blank=True, max_length=100)),
                ('street_line2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('zipcode', models.CharField(blank=True, max_length=5)),
                ('country', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': '3. Addresses',
            },
            bases=(models.Model, object),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('active', models.BooleanField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='client_Creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='client_modified_by', to=settings.AUTH_USER_MODEL)),
                ('primary_user', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '2. Clients',
            },
            bases=(models.Model, object),
        ),
        migrations.CreateModel(
            name='ClientType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('active', models.BooleanField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='clienttype_Creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='clienttype_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '1 ClientType',
            },
            bases=(models.Model, object),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('active', models.BooleanField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='person_Creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='person_modified_by', to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app_core.ClientType')),
                ('userId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, object),
        ),
        migrations.AddField(
            model_name='client',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='typeofclient', to='app_core.ClientType'),
        ),
        migrations.AddField(
            model_name='address',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clientAddresses', to='app_core.Client'),
        ),
        migrations.AddField(
            model_name='address',
            name='created_by',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='address_Creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='address',
            name='modified_by',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='address_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='client',
            unique_together={('type', 'primary_user')},
        ),
    ]
