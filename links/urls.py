from django.urls import path
from . import views

urlpatterns = [
    # Boshqa URLlar...
    path('ilmiyfaoliyatlar/<int:id>/download/', views.download_ilmiyfaoliyat, name='download_ilmiyfaoliyat'),
]
