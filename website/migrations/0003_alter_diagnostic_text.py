# Generated by Django 4.0.1 on 2022-01-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_diagnostic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostic',
            name='text',
            field=models.TextField(blank=True, help_text='text', max_length=200, null=True),
        ),
    ]
