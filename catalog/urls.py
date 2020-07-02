from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('patients/', views.PatientView.as_view(), name = 'patients'),
    path('patients/viewall',views.display_all,name='display'),
    path('patients/sortori',views.sortingori,name='sortingori'),
    path('patients/searchori',views.searchori,name='searchori'),
    path('patients/sort/<sortkey>',views.sorting, name='sorting'),
    path('patients/search/<searchkey>/<searchvalue>',views.search, name = 'search'),
    path('patients/add',views.add_patients, name='add_patients'),
    path('patients/delete/<int:pk>',views.delete_patients,name='delete_patients'),
    path('patients/<int:pk>', views.PatientDetailView.as_view(), name='patients-detail'),
    path('patients/<int:pk>/renew/', views.renew_patients, name='renew_patients'),
    path('patients/<int:pk>/json/',views.jsondata, name = 'json'),
]