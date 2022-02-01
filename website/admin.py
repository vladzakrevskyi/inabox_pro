from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from website.models import *


class DiagnosticBulgariaAdmin(SummernoteModelAdmin):
    summernote_field = ('desc')
    display = ('title')

    def has_add_permission(self, request):
        return False

class DiagnosticCyprusAdmin(SummernoteModelAdmin):
    summernote_field = ('desc')
    display = ('title')



class DiagnosticCryptoAdmin(SummernoteModelAdmin):
    summernote_field = ('desc')
    display = ('title')




admin.site.register(OurOffer)
admin.site.register(Step)
admin.site.register(Testimonial)
admin.site.register(DiagnosticBulgaria, DiagnosticBulgariaAdmin)
admin.site.register(DiagnosticCyprus, DiagnosticCyprusAdmin)
admin.site.register(DiagnosticCrypto, DiagnosticCryptoAdmin)