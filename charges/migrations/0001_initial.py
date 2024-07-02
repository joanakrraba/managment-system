# Generated by Django 5.0.6 on 2024-07-01 13:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task_management', '0004_remove_client_user_alter_client_active_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Backlog', 'Backlog'), ('In Progress', 'In Progress'), ('In Review', 'In Review'), ('Scheduled', 'Scheduled'), ('Done', 'Done')], default='Requested', max_length=225)),
                ('created_date', models.DateTimeField()),
                ('last_modified_date', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_costs', to='task_management.client')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_costs', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_modified_user_costs', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_costs', to='task_management.project')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_tasks', to='task_management.task')),
            ],
        ),
        migrations.CreateModel(
            name='CostApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('status', models.CharField(choices=[('Backlog', 'Backlog'), ('In Progress', 'In Progress'), ('In Review', 'In Review'), ('Scheduled', 'Scheduled'), ('Done', 'Done')], default='Draft', max_length=225)),
                ('created_date', models.DateTimeField()),
                ('last_modified_date', models.DateTimeField()),
                ('cost', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cost_approvals', to='charges.cost')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_cost_approvals', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_modified_user_cost_approvals', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_cost_approvals', to='task_management.task')),
            ],
        ),
    ]