# Generated by Django 4.2.5 on 2023-10-03 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testback', '0003_alter_listles_lesson_alter_listles_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listles',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listless', to='testback.lesson'),
        ),
    ]
