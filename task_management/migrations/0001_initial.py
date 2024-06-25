# Generated by Django 5.0.6 on 2024-06-25 12:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('deadlineDate', models.DateField()),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('Urgent', 'Urgent'), ('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Normal', max_length=225)),
                ('status', models.CharField(choices=[('Backlog', 'Backlog'), ('In Progress', 'In Progress'), ('In Review', 'In Review'), ('Scheduled', 'Scheduled'), ('Done', 'Done')], default='', max_length=225)),
                ('assegnee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assegnees', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks_created', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks_modified', to=settings.AUTH_USER_MODEL)),
                ('reporter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reporters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
