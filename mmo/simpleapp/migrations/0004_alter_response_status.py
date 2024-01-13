# Generated by Django 4.2.7 on 2024-01-05 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0003_alter_post_text_alter_response_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='status',
            field=models.CharField(choices=[('undefined', 'Неопределенный'), ('accepted', 'Принят'), ('rejected', 'Отклонен')], default='undefined', max_length=10),
        ),
    ]