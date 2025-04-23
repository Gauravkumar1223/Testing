from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    # path('entry/<int:year>/<int:month>/<int:day>/', views.entry_time, name='entry_time'),
    path('ajax-update-entry/', views.ajax_update_entry, name='ajax_update_entry'),
    path('auto-fill/', views.auto_fill, name='auto_fill'),
    path('superuser-dashboard/', views.superuser_dashboard, name='superuser_dashboard'),
    path('save-user/', views.save_user_data, name='save_user_data'),
    path('redirect-after-login/', views.post_login_redirect, name='post_login_redirect'),
    path('export-user-excel/', views.export_user_excel, name='export_user_excel'),
    path('export-all-users-excel/', views.export_all_users_excel, name='export_all_users_excel')

]
