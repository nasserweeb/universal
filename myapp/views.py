from django.shortcuts import render

# Create your views here.
def index(request):
   # data = models.compny2.objects.all()
    return render(request,'index.html',{})

def about(request):
    return render(request,'about.html',{})
def contact(request):
    return render(request,'contact.html',{})
def news(request):
    return render(request,'news.html',{})
def testimonial(request):
    return render(request,'testimonial.html',{})
def services(request):
    return render(request,'service.html',{})

