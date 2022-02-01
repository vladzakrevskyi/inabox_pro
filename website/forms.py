from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_for_pickup = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    device_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    ip_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required = False)

class CareerForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cv = forms.FileField(widget=forms.ClearableFileInput())
    cover_letter = forms.FileField(required = False)


class BusinessPremiumForm(forms.Form):
    industry = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    size = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
