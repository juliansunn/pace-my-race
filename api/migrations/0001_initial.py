# Generated by Django 3.2 on 2023-07-22 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('zip_code', models.IntegerField(max_length=5, unique=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.city')),
                ('coached_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='training_groups', to=settings.AUTH_USER_MODEL)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_api.group_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('distance', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('distance_unit', models.CharField(choices=[('km', 'Kilometers'), ('mi', 'Miles')], default='km', max_length=2)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('registration_open', models.BooleanField(default=True)),
                ('registration_deadline', models.DateTimeField(default=None)),
                ('race_start', models.DateTimeField()),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.city')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(choices=[(1, 'Alabama'), (2, 'Alaska'), (3, 'Arizona'), (4, 'Arkansas'), (5, 'California'), (6, 'Canal'), (7, 'Colorado'), (8, 'Connecticut'), (9, 'Delaware'), (10, 'District'), (11, 'Florida'), (12, 'Georgia'), (13, 'Guam'), (14, 'Hawaii'), (15, 'Idaho'), (16, 'Illinois'), (17, 'Indiana'), (18, 'Iowa'), (19, 'Kansas'), (20, 'Kentucky'), (21, 'Louisiana'), (22, 'Maine'), (23, 'Maryland'), (24, 'Massachusetts'), (25, 'Michigan'), (26, 'Minnesota'), (27, 'Mississippi'), (28, 'Missouri'), (29, 'Montana'), (30, 'Nebraska'), (31, 'Nevada'), (32, 'New Hampshire'), (33, 'New Jersey'), (34, 'New Mexico'), (35, 'New York'), (36, 'North Carolina'), (37, 'North Dakota'), (38, 'Ohio'), (39, 'Oklahoma'), (40, 'Oregon'), (41, 'Pennsylvania'), (42, 'Puerto Rico'), (43, 'Rhode Island'), (44, 'South Carolina'), (45, 'South Dakota'), (46, 'Tennessee'), (47, 'Texas'), (48, 'Utah'), (49, 'Vermont'), (50, 'Virgin Islands'), (51, 'Virginia'), (52, 'Washington'), (53, 'West Virginia'), (54, 'Wisconsin'), (55, 'Wyoming')])),
            ],
        ),
        migrations.CreateModel(
            name='PacingGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.group')),
                ('pace_target', models.TimeField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('api.group',),
        ),
        migrations.CreateModel(
            name='TrainingGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.group')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('api.group',),
        ),
        migrations.CreateModel(
            name='RaceRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.race')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='participants',
            field=models.ManyToManyField(related_name='races_participated', through='api.RaceRegistration', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='race',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.race'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='api.state'),
        ),
        migrations.AddField(
            model_name='user',
            name='home_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='city_runners', to='api.city'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
