from django.shortcuts import render


# Create your views here.
def jinjaprint(request):
    data = "These jinja tags are used to perform advanced tags"
    d = {"get":data}
    return render(request,"main.html",context=d)
