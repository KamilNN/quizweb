# Generated by Django 5.0.6 on 2024-05-27 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.CharField(max_length=100, verbose_name='Оригинал')),
                ('meaning', models.CharField(max_length=100, verbose_name='Перевод')),
            ],
            options={
                'verbose_name': 'Слово',
                'verbose_name_plural': 'Слова',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option1', models.CharField(max_length=100, verbose_name='Вариант 1')),
                ('option2', models.CharField(max_length=100, verbose_name='Вариант 2')),
                ('option3', models.CharField(max_length=100, verbose_name='Вариант 3')),
                ('correct_option', models.CharField(max_length=100, verbose_name='Верный ответ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.word', verbose_name='Слово')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]