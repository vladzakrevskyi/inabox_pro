# Generated by Django 4.0.1 on 2022-01-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_diagnostic_html_pay_pal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostic',
            name='html_pay_pal',
            field=models.TextField(blank=True, help_text='Add PayPal html', max_length=5000, null=True, verbose_name='Html PayPal'),
        ),
    ]