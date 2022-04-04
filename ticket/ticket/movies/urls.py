from django.urls import path
from movies import views

app_name='movies'
urlpatterns = [
    path('',views.movies,name='movies'),
    path('details/<slug:url>/',views.details,name='details'),
    path('book/<slug:url>/',views.book,name='book'),
    path('<slug:url>/seatbook/',views.seatbook,name='seatbook'),
    path('<slug:url>/ticket/',views.ticket,name='ticket'),
    path('confirmation/',views.confirmation,name='confirmation'),
]