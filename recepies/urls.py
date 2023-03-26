from django.urls import path
from recepies.views import home


urlpatterns = [
    path('', home),    
]
