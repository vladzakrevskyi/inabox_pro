# Generated by Django 4.0.1 on 2022-01-30 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_rename_diagnostic_diagnosticbulgaria'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosticCyprus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='Page title')),
                ('title_en', models.CharField(blank=True, max_length=500, null=True, verbose_name='Page title')),
                ('title_bg', models.CharField(blank=True, max_length=500, null=True, verbose_name='Page title')),
                ('desc', models.TextField(blank=True, help_text='Add some text', null=True, verbose_name='Text')),
                ('desc_en', models.TextField(blank=True, help_text='Add some text', null=True, verbose_name='Text')),
                ('desc_bg', models.TextField(blank=True, help_text='Add some text', null=True, verbose_name='Text')),
                ('html_pay_pal', models.TextField(blank=True, help_text='Add PayPal html', max_length=5000, null=True, verbose_name='Html PayPal')),
                ('html_field', models.TextField(blank=True, help_text='Add html', null=True, verbose_name='Html field')),
            ],
            options={
                'verbose_name': 'Diagnostic',
                'verbose_name_plural': 'Diagnostic',
            },
        ),
    ]