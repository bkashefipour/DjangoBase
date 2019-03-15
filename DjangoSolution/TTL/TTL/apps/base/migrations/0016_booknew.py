# Generated by Django 2.1.4 on 2019-03-14 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0015_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booknew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=128)),
                ('created_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='booknew_Creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, related_name='booknew_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, object),
        ),
    ]