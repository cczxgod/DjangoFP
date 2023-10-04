# Generated by Django 4.2.5 on 2023-10-01 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=60)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ListLes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Не просмотрено', max_length=20)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testback.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=30)),
                ('lessons', models.ManyToManyField(to='testback.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lessons', models.ManyToManyField(through='testback.ListLes', to='testback.lesson')),
                ('products', models.ManyToManyField(to='testback.product')),
            ],
        ),
        migrations.AddField(
            model_name='listles',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testback.user'),
        ),
    ]