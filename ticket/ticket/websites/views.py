from django.shortcuts import render
from movies.models import Movies,Slider

# Create your views here.
def index(request):
    try:
        __context = {}

        __context['movie'] = Movies.objects.filter(is_active=True).order_by('?')
        __context['slider'] = Slider.objects.filter(is_active=True).order_by('?')
        __context['topmovies'] = Movies.objects.filter(is_active=True)
        return render(request,'websites/index.html',__context)
    except Exception as error:
        print(error)
        return render(request,'websites/index.html',{'error':error})

def about(request):
    try:
        return render(request,'websites/about.html')
    except Exception as error:
        print(error)
        return render(request,'websites/about.html',{'error':error})