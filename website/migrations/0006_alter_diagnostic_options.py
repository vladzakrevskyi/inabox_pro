# Generated by Django 4.0.1 on 2022-01-18 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_diagnostic_htmlfield_alter_diagnostic_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diagnostic',
            options={'verbose_name': 'Diagnostic', 'verbose_name_plural': 'Diagnostic'},
        ),
    ]
