from django.urls import path
from Dear_Diary import views as dv
from Poll import views as pv


urlpatterns = [
    path('', dv.index,name='home'),
    path('poll/', pv.home,name='poll'),
    path('create/', pv.create,name='create'),
    path('vote/<poll_id>/', pv.vote,name='vote'),
    path('results/<poll_id>/', pv.results,name='results')
]


