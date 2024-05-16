# Generated by Django 4.2 on 2024-05-13 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0001_initial'),
        ('student_groups', '0001_initial'),
        ('students', '0002_student_student_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_group',
        ),
        migrations.AddField(
            model_name='student',
            name='direction_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directions.direction'),
        ),
        migrations.AddField(
            model_name='student',
            name='group_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student_groups.studentgroup'),
        ),
        migrations.AddField(
            model_name='student',
            name='rfid',
            field=models.CharField(max_length=30, null=True),
        ),
    ]