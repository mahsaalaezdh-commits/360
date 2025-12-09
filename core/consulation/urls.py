from django.urls import path
from . import views

app_name = 'consulation'

urlpatterns = [
    path('', views.consultation_view, name='consultation_form'),
]
