from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("change-password", views.change_password, name="change_password"),
    path("logout", views.logout_request, name="logout"),
    path("show-profile", views.show_profile, name="show_profile"),
    path("show-participant/<int:id>", views.show_participant, name="show_participant"),
    path("edit-profile/<int:id>", views.edit_profile, name="edit_profile"),
    
    path("reset_password/", auth_views.PasswordResetView.as_view(template_name="account/password_reset.html"), name="reset_password"),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_sent.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html"), name="password_reset_confirm"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_done.html"), name="password_reset_complete"),
]