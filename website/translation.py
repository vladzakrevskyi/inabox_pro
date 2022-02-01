from modeltranslation.translator import translator, register, TranslationOptions
from .models import *

@register(OurOffer)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Step)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Testimonial)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'text')


@register(DiagnosticBulgaria)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('desc', 'title')

@register(DiagnosticCyprus)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('desc', 'title')

@register(DiagnosticCrypto)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('desc', 'title')