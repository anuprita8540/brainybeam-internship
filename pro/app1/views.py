from django.shortcuts import render,HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("this is my first view function")

def demo(request):
    return render(request,'demo.html')