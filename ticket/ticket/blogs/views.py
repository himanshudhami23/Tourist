from django.shortcuts import render

# Create your views here.
def blogs(request):
    try:
        return render(request,'blogs/blogs.html')
    except Exception as error:
        print(error)
        return render(request,'blogs/blogs.html',{'error':error})

def details(request):
    try:
        return render(request,'blogs/details.html')
    except Exception as error:
        print(error)
        return render(request,'blogs/details.html',{'error':error})