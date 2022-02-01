# Generated by Django 4.0.1 on 2022-01-21 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_diagnostic_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostic',
            name='desc_en',
            field=models.TextField(blank=True, help_text='Add some text', null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='title_en',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Page title'),
        ),
    ]
