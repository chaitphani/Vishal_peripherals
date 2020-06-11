from django.urls import path
from cheetaapp import views


urlpatterns = [
    path('', views.make_card, name='card_create'),
    path('list', views.data_card, name='card_list'),

]