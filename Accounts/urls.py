from django.urls import path
from Accounts import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('signup/',views.Signup,name='signup'),
    path('login/',views.User_login,name='login'),
    path('dashboard/',views.User_Dashboard,name='dashboard'),
    path('logout/',views.User_Logout,name='logout'),
    path('change-passwd/',views.Change_Password,name='change_password'),
    path('update-profile/',views.EditProfiles,name='editprofile'),

    # Reset Password here..
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='resetPasswd/password_reset_form.html', form_class=MyPasswordResetForm), name='reset_password'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='resetPasswd/password_reset_done.html'),name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='resetPasswd/password_reset_confirm.html',form_class=MySetPasswordForm ),name='password_reset_confirm'),
    path('password-reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='resetPasswd/password_reset_complete.html'),name='password_reset_complete'),

    # path('password-reset/confirm/'),

    


] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
