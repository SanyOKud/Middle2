from django.urls import path
from . import views2

urlpatterns = (
    path('', views2.index, name='home'),
    path('user/', views2.user_info2, name='user_info'),
    path('team/', views2.team_info, name='team_info'),
    path('contact/', views2.contact_info, name='contact_info'),
    path('table_in/', views2.TableInTarget_list, name='table_in'),
    path('table_out/', views2.table_out, name='table_out'),
    # path('user/<int:user_id>/', views2.user_info, name='user_info'),

)
