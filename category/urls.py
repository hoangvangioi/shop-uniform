from django.urls import path
from .views import *


urlpatterns = [
    # path('', include('store.urls'))
    path('add_category/', CategoryCreateView.as_view(), name='add_category')
]
