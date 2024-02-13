from django.urls import path
from .views import CompanyView

urlpatterns = [
   path('companies/list', CompanyView.as_view(), name='companies_list'),
   path('companies/save', CompanyView.as_view(), name='companies_save'),
   path('companies/<int:id>', CompanyView.as_view(), name='companies_process'),
]
