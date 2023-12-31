# Generated by Django 4.2.5 on 2023-10-04 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта для рассылки')),
                ('full_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Имя')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='MailingMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250, verbose_name='Тема')),
                ('message', models.TextField(verbose_name='текст')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
            },
        ),
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='Начало рассылки')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='Конец рассылки')),
                ('period', models.CharField(choices=[('Ежедневная', 'Ежедневная'), ('Раз в неделю', 'Раз в неделю'), ('Раз в месяц', 'Раз в месяц')], default='Ежедневная', max_length=20, verbose_name='Периодичность')),
                ('status', models.CharField(choices=[('Запущена', 'Создана'), ('Создана', 'Запущена'), ('Завершена', 'Завершена')], default='Создана', max_length=20, verbose_name='Статус рассылки')),
                ('clients', models.ManyToManyField(to='client.client', verbose_name='клиенты')),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.mailingmessage', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ok', 'Успешно'), ('failed', 'Ошибка')], default='ok', verbose_name='Статус попытки')),
                ('last_try', models.DateTimeField(auto_now_add=True, verbose_name='Дата последней попытки')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='ответ')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client', verbose_name='Клиент')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.mailingsettings', verbose_name='Настройка')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
    ]
