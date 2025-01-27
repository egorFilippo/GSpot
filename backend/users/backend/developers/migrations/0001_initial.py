# Generated by Django 4.1.7 on 2023-03-22 09:48

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                (
                    'last_login',
                    models.DateTimeField(blank=True, null=True, verbose_name='last login'),
                ),
                (
                    'username',
                    models.CharField(
                        error_messages={'unique': 'A user with that username already exists.'},
                        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                        max_length=150,
                        unique=True,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                        verbose_name='username',
                    ),
                ),
                (
                    'first_name',
                    models.CharField(blank=True, max_length=150, verbose_name='first name'),
                ),
                (
                    'last_name',
                    models.CharField(blank=True, max_length=150, verbose_name='last name'),
                ),
                (
                    'is_staff',
                    models.BooleanField(
                        default=False,
                        help_text='Designates whether the user can log into this admin site.',
                        verbose_name='staff status',
                    ),
                ),
                (
                    'date_joined',
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name='date joined'
                    ),
                ),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('phone', models.CharField(max_length=12)),
                ('avatar', models.ImageField(blank=True, upload_to='')),
                ('is_banned', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_superuser', models.BooleanField(default=False)),
                (
                    'country',
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.country'
                    ),
                ),
                ('friends', models.ManyToManyField(to='developers.companyuser')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('icon', models.ImageField(blank=True, upload_to='')),
                ('value', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'developer contact type',
                'verbose_name_plural': 'developer contact types',
                'db_table': 'developer_contact_type',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeveloperContentType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=50)),
                ('app_label', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'developer content type',
                'verbose_name_plural': 'developer content types',
                'db_table': 'developer_content_type',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeveloperGroup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'developer group',
                'verbose_name_plural': 'developer groups',
                'db_table': 'developer_group',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeveloperPermission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('code_name', models.CharField(max_length=50)),
                (
                    'content_type',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='developers.developercontenttype',
                    ),
                ),
            ],
            options={
                'verbose_name': 'developer permission',
                'verbose_name_plural': 'developer permissions',
                'db_table': 'developer_permission',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeveloperUserPermissions',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    'permission',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to='developers.developerpermission',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to='developers.companyuser'
                    ),
                ),
            ],
            options={
                'verbose_name': 'developer user permission',
                'verbose_name_plural': 'developer user permissions',
                'db_table': 'developer_user_permission',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeveloperGroupUserPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                (
                    'group',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to='developers.developergroup'
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to='developers.companyuser'
                    ),
                ),
            ],
            options={
                'verbose_name': 'developer group user permission',
                'verbose_name_plural': 'developer group user permissions',
                'db_table': 'developer_group_user_permission',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeveloperGroupPermission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                (
                    'group',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to='developers.developergroup'
                    ),
                ),
                (
                    'permission',
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to='developers.developerpermission',
                    ),
                ),
            ],
            options={
                'verbose_name': 'developer group permission',
                'verbose_name_plural': 'developer group permissions',
                'db_table': 'developer_group_permission',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('is_confirmed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                (
                    'contacts',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='developers.contacttype'
                    ),
                ),
                (
                    'created_by',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT, to='developers.companyuser'
                    ),
                ),
            ],
        ),
    ]
