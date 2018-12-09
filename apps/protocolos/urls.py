from django.urls import path
from .views import ProtocolosList

urlpatterns = [
    path('', ProtocolosList.as_view, name='protocolos_list'),
]
