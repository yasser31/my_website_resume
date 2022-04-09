from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name ="dashboard"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('success/', views.ContactSuccessView.as_view(), name="success"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)