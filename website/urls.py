from django.contrib import admin
from django.urls import include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home_page"),
    path('success_page/', views.success_page, name="success_page"),
    path('terms_and_conditions/', views.terms_and_conditions, name="terms_page"),
    path('business-premium/', views.business_premium, name="business_page"),
    path('diagnostic-bulgaria/', views.diagnostic_bulgaria, name="diagnostic_bulgaria_page"),
    path('diagnostic-cyprus/', views.diagnostic_cyprus, name="diagnostic_cyprus_page"),
    path('diagnostic-crypto/', views.diagnostic_crypto, name="diagnostic_crypto_page"),
    path('summernote/', include('django_summernote.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)