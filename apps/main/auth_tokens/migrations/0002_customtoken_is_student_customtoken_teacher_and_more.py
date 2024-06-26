# Generated by Django 4.2 on 2024-05-24 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_alter_teacher_login_alter_teacher_password'),
        ('exam_schedule', '0003_alter_examschedule_room'),
        ('auth_tokens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtoken',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customtoken',
            name='teacher',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_auth_token', to='teachers.teacher', verbose_name='Teacher'),
        ),
        migrations.AlterField(
            model_name='customtoken',
            name='schedule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule_auth_token', to='exam_schedule.examschedule', verbose_name='Exam Schedule'),
        ),
    ]
