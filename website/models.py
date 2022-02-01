from django.db import models


class OurOffer(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    color = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title


class Step(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Users/', help_text='User image')
    text = models.TextField(max_length=2000)
    fb_url = models.CharField(max_length=200, null=True, blank=True)
    ldn_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class DiagnosticBulgaria(models.Model):
    title = models.CharField('Page title', null=False, blank=True, max_length=500)
    desc = models.TextField('Text', null=True, blank=True, help_text='Add some text')
    html_pay_pal = models.TextField('Html PayPal', max_length=5000, null=True, blank=True, help_text='Add PayPal html')
    html_field = models.TextField('Html field', null=True, blank=True, help_text='Add html')

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name = 'Diagnostic Bulgaria'
        verbose_name_plural = 'Diagnostic Bulgaria'

class DiagnosticCyprus(models.Model):
    title = models.CharField('Page title', null=False, blank=True, max_length=500)
    desc = models.TextField('Text', null=True, blank=True, help_text='Add some text')
    html_pay_pal = models.TextField('Html PayPal', max_length=5000, null=True, blank=True, help_text='Add PayPal html')
    html_field = models.TextField('Html field', null=True, blank=True, help_text='Add html')

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name = 'Diagnostic Cyprus'
        verbose_name_plural = 'Diagnostic Cyprus'

class DiagnosticCrypto(models.Model):
    title = models.CharField('Page title', null=False, blank=True, max_length=500)
    desc = models.TextField('Text', null=True, blank=True, help_text='Add some text')
    html_pay_pal = models.TextField('Html PayPal', max_length=5000, null=True, blank=True, help_text='Add PayPal html')
    html_field = models.TextField('Html field', null=True, blank=True, help_text='Add html')

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name = 'Diagnostic Crypto'
        verbose_name_plural = 'Diagnostic Crypto'
