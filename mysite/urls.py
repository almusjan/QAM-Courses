from django.urls import path
from . import views

app_name = 'site'
urlpatterns = [
    path('', views.index, name='index'),
    path('sites/', views.sites_list, name='sites_list'),
    path('site/<int:site_id>/', views.site_info, name='site_info'),
    path('favorites/', views.favorites, name='favorites'),
    path('toggle-favorite/<int:site_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('contact/', views.contact, name='contact'),
    path('user-reports/', views.user_reports, name='user_reports'),
    path('manager-reports/', views.manager_reports, name='manager_reports'),
    path('report/<int:report_id>', views.report_info, name='report_info'),
]