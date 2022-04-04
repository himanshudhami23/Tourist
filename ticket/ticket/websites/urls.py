from django.urls import path
from websites import views

app_name='websites'
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
]