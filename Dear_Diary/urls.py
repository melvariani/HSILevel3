from django.urls import path
from Dear_Diary import views as dv
from TheWeather import views as wv
from Poll import views as pv


urlpatterns = [
    path('', dv.index,name="home"),
    path('diary/',dv.diary, name="diary"),
    path('add/', dv.add,name="add"),
    path('weather/',wv.index, name="weather"),
    path('delete/<city_name>',wv.delete_city, name='delete_city'),
    path('poll/', pv.home,name='poll'),
    path('create/', pv.create,name='create'),
    path('vote/<poll_id>/', pv.vote,name='vote'),
    path('results/<poll_id>/', pv.results,name='results')
]




