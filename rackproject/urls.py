from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("rackapp.urls")),
    path("", include("accounts.urls")),
    path("admin/", admin.site.urls),
    path("password_reset/",
         auth_views.PasswordResetView.as_view(
         template_name = "password_reset.html"),
         name = "password_reset"),
    path("password_reset/done/",
         auth_views.PasswordResetDoneView.as_view(
         template_name = "password_reset_sent.html"),
         name = "password_reset_done"),
    path("reset/<uidb64>/<token>",
         auth_views.PasswordResetConfirmView.as_view(
             template_name = "password_reset_form.html"),
         name = "password_reset_confirm"),
    path("reset/done/",
         auth_views.PasswordResetCompleteView.as_view(
             template_name = "password_reset_done.html"),
         name = "password_reset_complete"),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT
)