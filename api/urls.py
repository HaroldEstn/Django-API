from django.urls import path
from .views import PersonView

urlpatterns = [
        path('people/', PersonView.as_view(), name='people_list'),
        path('people/<int:id>', PersonView.as_view(), name='people_process')
        ]
