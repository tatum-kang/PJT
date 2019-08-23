from django.shortcuts import render
from .models import Movies
# Create your views here.
def index(request):
    movies = Movies.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def create(request):
    Movies.objects.create(title=request.GET.get('title'), title_en=request.GET.get('title_en'), audience=request.GET.get('audience'), open_date=request.GET.get('open_date'), genre=request.GET.get('genre'), watch_grade=request.GET.get('watch_grade'), score=request.GET.get('score'), poster_url=request.GET.get('poster_url'), description=request.GET.get('description'))
    return render(request, 'movies/create.html')


def new(request):
    return render(request, 'movies/new.html')


def select(request, pk_num):
    select_movie = Movies.objects.get(pk=pk_num) 
    context = {
        'select_movie': select_movie,
    }
    return render(request, 'movies/select.html', context)


def edit(request, pk_num):
    edit_movie = Movies.objects.get(pk=pk_num)
    context = {
        'edit_movie': edit_movie,
        'pk_num': pk_num,
    }
    return render(request, 'movies/edit.html', context)


def update(request, pk_num):
    update_movie = Movies.objects.get(pk=pk_num)
    update_movie.title = request.GET.get('title')
    update_movie.title_en = request.GET.get('title_en')
    update_movie.audience = request.GET.get('audience')
    update_movie.open_date = request.GET.get('open_date')
    update_movie.genre = request.GET.get('genre')
    update_movie.watch_grade = request.GET.get('watch_grade') 
    update_movie.score = request.GET.get('score')
    update_movie.poster_url = request.GET.get('poster_url')
    update_movie.description = request.GET.get('description')
    update_movie.save()
    return render(request, 'movies/update.html')


def delete(request, pk_num):
    delete_movie = Movies.objects.get(pk=pk_num)
    delete_movie.delete()
    return render(request, 'movies/delete.html')
