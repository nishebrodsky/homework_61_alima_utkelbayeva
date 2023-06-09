# Generated by Django 4.1.6 on 2023-03-16 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('In progress', 'In Progress'), ('New', 'New'), ('Done', 'Done')], default='New', max_length=100, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Task', 'Task'), ('Bag', 'Bug'), ('Enhancement', 'Enhancement')], default='Task', max_length=100, verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='statuses', to='webapp.status', verbose_name='Status')),
                ('type', models.ManyToManyField(blank=True, related_name='types', to='webapp.type', verbose_name='Type')),
            ],
        ),
    ]
