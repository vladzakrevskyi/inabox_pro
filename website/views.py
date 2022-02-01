from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
from io import StringIO
from .models import *
from .forms import *
import csv


def render_tamplate(tpl, dt, request):
    dct = {}
    dct.update(dt)
    return render(request, tpl, dct)


def career_form(request):
    cr_form = CareerForm(request.POST, request.FILES)
    if request.method == 'POST' and cr_form.is_valid():
        name = cr_form.cleaned_data['name']
        email = cr_form.cleaned_data['email']
        phone = cr_form.cleaned_data['phone']
        cv = request.FILES['cv']
        if 'cover_letter' in request.FILES:
            cover_letter = request.FILES['cover_letter']
        else:
            cover_letter = False
        recipients = ['careers@inabox.pro']
        headers = {'Reply-To': email}
        try:
            email = EmailMessage(
                "[In A Box] Career Form",
                "Career Form Contact \n\nName: %s \nEmail: %s \nPhone: %s\n"
                % (name, email, phone),
                'support@inabox.pro',
                recipients,
                headers=headers
                )
            email.attach(cv.name, cv.read(), cv.content_type)
            if 'cover_letter' in request.FILES:
                email.attach(cover_letter.name, cover_letter.read(), cover_letter.content_type)
            email.send()
            subject = '[In A Box] Career contact'
            html_message = render_to_string('email/email_career.html')
            plain_message = strip_tags(html_message)
            from_email = 'support@inabox.pro'
            to = [cr_form.cleaned_data['email']]
            mail.send_mail(subject, plain_message, from_email, to, html_message=html_message)
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return redirect('/success_page')


def business_premium_form(request):
    bp_form = BusinessPremiumForm(request.POST)
    if bp_form.is_valid():
        industry = bp_form.cleaned_data['industry']
        size = bp_form.cleaned_data['size']
        name = bp_form.cleaned_data['name']
        email = bp_form.cleaned_data['email']
        phone = bp_form.cleaned_data['phone']
        recipients = ['bsp@inabox.pro']
        headers = {'Reply-To': email}
        try:
            email = EmailMessage(
                "[In A Box] Businness Form",
                "Business Form Contact \n\nIndustry: %s \nSize: %s \nName: %s\n E-mail: %s\n Phone: %s\n"
                % (industry, size, name, email, phone),
                'support@inabox.pro',
                recipients,
                headers=headers
                )
            email.send()
            subject = '[In A Box] Business premium contact'
            html_message = render_to_string('email/email_business.html')
            plain_message = strip_tags(html_message)
            from_email = 'support@inabox.pro'
            to = [bp_form.cleaned_data['email']]
            mail.send_mail(subject, plain_message, from_email, to, html_message=html_message)
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return redirect('/success_page')


def contact_form(request):
    fl_form = ContactForm(request.POST)
    if fl_form.is_valid():
        name = fl_form.cleaned_data['name']
        email = fl_form.cleaned_data['email']
        phone = fl_form.cleaned_data['phone']
        country = fl_form.cleaned_data['country']
        date = fl_form.cleaned_data['date_for_pickup']
        device_type = fl_form.cleaned_data['device_type']
        ip_address = fl_form.cleaned_data['ip_address']
        csvfile = StringIO()
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Name', 'Email', 'Phone', 'Country', 'Date', 'Device type', 'Ip address'])
        csvwriter.writerow([name, email, phone, country, date, device_type, ip_address])
        recipients = ['webrequests@inabox.pro']
        headers = {'Reply-To': email}
        try:
            email = EmailMessage(
                "[In A Box] Request contact",
                "Request Form Contact \n\nName: %s \nEmail: %s \nPhone: %s \nCountry: %s \nDate: %s \nDevice Type: %s \nIp address: %s\n"
                "\n\nPlease don't reply to this message. "
                "For the answer use the e-mail specified by the client."
                % (name, email, phone, country, date, device_type, ip_address), 'support@inabox.pro', recipients, headers=headers)
            email.attach('web_request.csv', csvfile.getvalue(), 'text/csv')
            email.send()
            subject = '[In A Box] Contact'
            html_message = render_to_string('email/email_contact.html')
            plain_message = strip_tags(html_message)
            from_email = 'support@inabox.pro'
            to = [fl_form.cleaned_data['email']]
            mail.send_mail(subject, plain_message, from_email, to, html_message=html_message)
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return redirect('/success_page')


def home(request):
    offers = OurOffer.objects.all()
    steps = Step.objects.all()
    testimonials = Testimonial.objects.all()
    if request.method == 'POST':
        fl_form = ContactForm(request.POST)
        cr_form = CareerForm(request.POST, request.FILES)
        if fl_form.is_valid():
            return contact_form(request)
        elif cr_form.is_valid():
            return career_form(request)
        return render_tamplate('index.html', {'offers': offers, 'steps': steps,
                                              'testimonials': testimonials}, request)
    else:
        return render_tamplate('index.html', {'offers': offers, 'steps': steps,
                                              'testimonials': testimonials}, request)


def success_page(request):
    if request.method == 'POST':
        fl_form = ContactForm(request.POST)
        cr_form = CareerForm(request.POST, request.FILES)
        if fl_form.is_valid():
            return contact_form(request)
        elif cr_form.is_valid():
            return career_form(request)
        return render_tamplate('success_page.html', {}, request)
    else:
        return render_tamplate('success_page.html', {}, request)


def terms_and_conditions (request):
    if request.method == 'POST':
        fl_form = ContactForm(request.POST)
        cr_form = CareerForm(request.POST, request.FILES)
        if fl_form.is_valid():
            return contact_form(request)
        elif cr_form.is_valid():
            return career_form(request)
        return render_tamplate('terms_and_conditions.html', {}, request)
    else:
        return render_tamplate('terms_and_conditions.html', {}, request)


def business_premium(request):
    if request.method == 'POST':
        fl_form = ContactForm(request.POST)
        bp_form = BusinessPremiumForm(request.POST)
        cr_form = CareerForm(request.POST, request.FILES)
        if fl_form.is_valid():
            return contact_form(request)
        elif bp_form.is_valid():
            return business_premium_form(request)
        elif cr_form.is_valid():
            return career_form(request)
        return render_tamplate('business_premium.html', {}, request)
    else:
        return render_tamplate('business_premium.html', {}, request)

def diagnostic_bulgaria(request):
    diagnostics = DiagnosticBulgaria.objects.all()
    dct = {'diagnostic': diagnostics}
    if request.method == 'POST':
        fl_form = ContactForm(request.POST)
        cr_form = CareerForm(request.POST, request.FILES)
        if fl_form.is_valid():
            return contact_form(request)
        elif cr_form.is_valid():
            return career_form(request)
        return render_tamplate('diagnostic_bulgaria.html', dct, request)
    else:
        return render_tamplate('diagnostic_bulgaria.html', dct, request)

def diagnostic_cyprus(request):
    diagnostics = DiagnosticCyprus.objects.all()
    dct = {'diagnostic': diagnostics}
    if request.method == 'POST':
        fl_form = ContactForm(request.POST)
        cr_form = CareerForm(request.POST, request.FILES)
        if fl_form.is_valid():
            return contact_form(request)
        elif cr_form.is_valid():
            return career_form(request)
        return render_tamplate('diagnostic_cyprus.html', dct, request)
    else:
        return render_tamplate('diagnostic_cyprus.html', dct, request)

def diagnostic_crypto(request):
    diagnostics = DiagnosticCrypto.objects.all()
    dct = {'diagnostic': diagnostics}
    if request.method == 'POST':
        fl_form = ContactForm(request.POST)
        cr_form = CareerForm(request.POST, request.FILES)
        if fl_form.is_valid():
            return contact_form(request)
        elif cr_form.is_valid():
            return career_form(request)
        return render_tamplate('diagnostic_crypto.html', dct, request)
    else:
        return render_tamplate('diagnostic_crypto.html', dct, request)
