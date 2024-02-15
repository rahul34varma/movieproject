from django.shortcuts import render
from testapp.forms import movieform
from testapp.models import movie


# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')

def add_movie_view(request):
    form=movieform()
    if request.method=='POST':
        form=movieform(request.POST)
        if form.is_valid():
            form.save()
        return index_view(request)
    return render(request,'testapp/addmovies.html',{'form':form})
def list_movie_view(request):
    movies_list=movie.objects.all()
    return render(request,'testapp/listmovie.html',{'movies_list':movies_list})




