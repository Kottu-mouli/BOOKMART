from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_pdf_page/<int:pk>/', views.view_pdf_page, name='view_pdf_page'),
    
]
