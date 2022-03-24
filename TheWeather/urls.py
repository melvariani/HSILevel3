from django.urls import path
from Dear_Diary import views as dv
from TheWeather import views as wv


urlpatterns = [
    path('weather/',wv.index,name='weather'),
    path('delete/<city_name>',wv.delete_city, name='delete_city'),
    path('', dv.index,name="home")
]
