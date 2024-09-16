# Generated by Django 5.1.1 on 2024-09-16 04:43

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_leave_date_profile_leave_type_profile_reason_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='leave_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='leave_type',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='reason',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='request_date',
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('casual', 'Casual Leave'), ('sick', 'Sick Leave'), ('other', 'Other')], max_length=10)),
                ('leave_date', models.DateField()),
                ('reason', models.TextField()),
                ('request_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leave_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
