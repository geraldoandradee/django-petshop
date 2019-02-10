# -*- coding:utf-8 -*-
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
            name='PetDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name of the pet')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of birth of pet')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pet_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Pet Details',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='PetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Type of the pet')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is pet type active')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Pet Types',
                'ordering': ('-id',),
            },
        ),
    ]
