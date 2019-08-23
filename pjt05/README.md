# Project 5 - Django

### |Project Goal

- 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작
- Python Web Framework를 통한 데이터 조작
- Object Relational Mapping에 대한 이해
- Template Variable을 활용한 Template 제작
- 영화 추천 사이트의 영화 정보 데이터 관리



### |Contents

## 1. Django

#### 주요 코드 내용

- model.py
​
  ```python
  from django.db import models
  
  # Create your models here.
  class Movie(models.Model):
      title = models.CharField(max_length=50)
      title_en = models.CharField(max_length=50)
      audience = models.IntegerField()
      open_date = models.DateTimeField()
      genre = models.CharField(max_length=50)
      watch_grade = models.CharField(max_length=50)
      score = models.FloatField()
      poster_url = models.TextField()
      description = models.TextField()
  
      def __str__(self):
          return self.title
  ```

​
​
​
​
- admin.py
​
  ```python
  from django.contrib import admin
  from .models import Movie
  
  # Register your models here.
  @admin.register(Movie)
  class MovieAdmin(admin.ModelAdmin):
      list_display = ('title', 'title_en', 'audience', 'open_date', 'genre', 'watch_grade', 'score', 'poster_url', 'description',)
  ```

  


​
​
* view.py
​
  ```python
  from django.shortcuts import render
  from .models import Movie
  
  # Create your views here.
  def index(request):
      movies = Movie.objects.all()
      return render(request, 'movie/index.html', {'movies':movies})
  
  
  def new(request):
      return render(request, 'movie/new.html')
  
  
  def create(request):
      title = request.GET.get('title')
      title_en = request.GET.get('title_en')
      audience = request.GET.get('audience')
      open_date = request.GET.get('open_date')
      genre = request.GET.get('genre')
      watch_grade = request.GET.get('watch_grade')
      score = request.GET.get('score')
      poster_url = request.GET.get('poster_url')
      description = request.GET.get('description')
  
      movie = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
      movie.save()
  
      return render(request, 'movie/create.html')
  
  
  def detail(request, movie_pk):
      movie = Movie.objects.get(pk=movie_pk)
      context = {
          'movie': movie,
          'title': movie.title,
          'title_en': movie.title_en,
          'audience': movie.audience,
          'open_date': movie.open_date,
          'genre': movie.genre,
          'watch_grade': movie.watch_grade,
          'score': movie.score,
          'poster_url': movie.poster_url,
          'description': movie.description,
      }
      
      
  
      return render(request, 'movie/detail.html', context)
  
  
  def edit(request, movie_pk):
      movie = Movie.objects.get(pk=movie_pk)
  
      return render(request, 'movie/edit.html', {'movie': movie})
  
  def update(request, movie_pk):
      title = request.GET.get('title')
      title_en = request.GET.get('title_en')
      audience = request.GET.get('audience')
      open_date = request.GET.get('open_date')
      genre = request.GET.get('genre')
      watch_grade = request.GET.get('watch_grade')
      score = request.GET.get('score')
      poster_url = request.GET.get('poster_url')
      description = request.GET.get('description')
  
      movie = Movie.objects.get(pk=movie_pk)
      movie.save()
      return render(request, 'movie/update.html')
  
  
  def delete(request, movie_pk):
      movie = Movie.objects.get(pk=movie_pk)
      movie.delete()
      return render(request, 'movie/delete.html')
  ```
  
  


​
​
- [Project]/urls.py
​
  ```python
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('movie/', include('movie.urls')),
  ]
  ```
  
- [App]/urls.py
​
  ```python
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('', views.index, name="index"),
      path('new/', views.new, name="new"),
      path('create/', views.create, name="create"),
      path('<int:movie_pk>/', views.detail, name="detail"),
      path('<int:movie_pk>/edit/', views.edit, name="edit"),
      path('<int:movie_pk>/update/', views.update, name="update"),
      path('<int:movie_pk>/delete/', views.delete, name="delete"),
  ]
  ```

  


​
​
​
​
## 2. HTML

#### 주요 코드 내용

* index.html
​
  ```html
  {% extends 'base.html' %}
  
  {% block title %}Index{% endblock  %}
  {% block content %}
  <h1>Movie List</h1>
  <a href="/movie/new/">영화정보생성</a>
  <ul>
    {% for movie in movies %}
    <li> <a href="/movie/{{ movie.pk }}">{{ movie.title }}</a></li>
    <li>{{ movie.score }}</li>
    {% endfor %}
  </ul>
  
  <p></p>
  {% endblock  %}
  ```
  
  


​
​
- new.html
​
  ```html
  {% extends 'base.html' %}
  
  {% block title %}New{% endblock  %}
  {% block content %}
  <form action="/movie/create/">
    <p>영화명 = <input id="title" type="text" name="title"></p>
    <p>영화명(영문) = <input id="title_en" type="text" name="title_en"></p>
    <p>누적관객수 = <input id="audience" type="number" name="audience"></p>
    <p>개봉일 = <input id="open_date" type="date" name="open_date"></p>
    <p>장르 = <input id="genre" type="text" name="genre"></p>
    <p>관람등급 = <input id="watch_grade" type="text" name="watch_grade"></p>
    <p>평점 = <input id="score" type="number" name="score"></p>
    <p>포스터이미지URL = <input id="poster_url" type="text" name="poster_url"></p>
    <p>영화소개 = <textarea name="description" id="description" cols="30" rows="10"></textarea></p>
  
    <button type="submit">영화 정보 생성</button>
  </form>
  {% endblock  %}
  ```
  


​
​
​
​
- edit.html
​
  ```html
  {% extends 'base.html' %}
  
  {% block title %}Edit{% endblock  %}
  {% block content %}
    <form action="/movie/{{ movie.pk }}/update/">
      <p>영화명 = <input id="title" type="text" name="title" value="{{ movie.title }}"></p>
      <p>영화명(영문) = <input id="title_en" type="text" name="title_en" value="{{ movie.title_en }}"></p>
      <p>누적관객수 = <input id="audience" type="number" name="audience" value="{{ movie.audience }}"></p>
      <p>개봉일 = <input id="open_date" type="date" name="open_date" value="{{ movie.open_date|date:"Y-m-d" }}"></p>
      <p>장르 = <input id="genre" type="text" name="genre" value="{{ movie.genre }}"></p>
      <p>관람등급 = <input id="watch_grade" type="text" name="watch_grade" value="{{ movie.watch_grade }}"></p>
      <p>평점 = <input id="score" type="number" name="score" value="{{ movie.score }}"></p>
      <p>포스터이미지URL = <input id="poster_url" type="text" name="poster_url" value="{{ movie.poster_url }}"></p>
      <p>영화소개 = <textarea name="description" id="description" cols="30" rows="10" >{{ movie.description }}</textarea></p>
  
      <button type="submit">수정하기</button>
    </form>
  {% endblock  %}
  ```

​
​
​
​
- detail.html
​
  ```html
  {% extends 'base.html' %}
  
  {% block title %}Detail View{% endblock  %}
  
  {% block content %}
  <h1> 영화명 = {{ movie.title }} </h1>
  <p>영화명(영문) = {{ movie.title_en }} </p>
  <p>누적관객수 = {{ movie.audience }} </p>
  <p>개봉일 = {{ movie.open_date|date:"Y-m-d" }} </p>
  <p>장르 = {{ movie.genre }} </p>
  <p>관람등급 = {{ movie.watch_grade }} </p>
  <p>평점 = {{ movie.score }} </p>
  <p>포스터이미지URL = {{ movie.poster_url }} </p>
  <p>영화소개 = {{ movie.description }} </p>
  
  <a href="/movie/">목록</a>
  <a href="/movie/{{ movie.pk }}/edit/">수정</a>
  <a href="/movie/{{ movie.pk }}/delete/">삭제</a>
  {% endblock  %}
  ```