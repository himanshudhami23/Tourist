from django.shortcuts import render
from .models import Movies,Actress_Images
# Create your views here.
def movies(request):
    try:
        return render(request,'movies/movies.html')
    except Exception as error:
        print(error)
        return render(request,'movies/movies.html',{'error':error})

def details(request,url):
    try:
        __context = {}

        __context['movie'] = Movies.objects.get(url=url)
        __context['acctress'] = Actress_Images.objects.filter(movie__url=url)
        return render(request,'movies/details.html',__context)
    except Exception as error:
        print(error)
        return render(request,'movies/details.html',{'error':error})

def book(request,url):
    try:
        __context = {}

        __context['book'] = Movies.objects.get(url=url)
        return render(request,'movies/book.html',__context)
    except Exception as error:
        print(error)
        return render(request,'movies/book.html',{'error':error})

def seatbook(request,url):
    try:
        __context = {}

        __context['seat'] = Movies.objects.get(url=url)
        return render(request,'movies/seat_book.html',__context)
    except Exception as error:
        print(error)
        return render(request,'movies/seat_book.html',{'error':error})

def ticket(request,url):
    try:
        __context = {}

        __context['ticket'] = Movies.objects.get(url=url)
        return render(request,'movies/ticket.html',__context)
    except Exception as error:
        print(error)
        return render(request,'movies/ticket.html',{'error':error})

def confirmation(request):
    try:
        return render(request,'movies/confirmation.html')
    except Exception as error:
        print(error)
        return render(request,'movies/confirmation.html',{'error':error})