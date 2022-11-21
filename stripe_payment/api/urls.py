from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('item/<int:item_id>/', views.get_item, name='get_item'),
    path('buy/<int:item_id>/', views.buy_item, name='buy_item'),
]
