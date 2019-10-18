# Project 6 - Django

### |Project Goal

- Python Web Framework를 통한 데이터 조작
- Object Relational Mapping에 대한 이해
- Template Variable을 활용한 Template 제작
- Static 파일 관리



### |Contents

## 1. Django 

#### 주요 코드 내용 - Movies (application)

- model.py
​
  
  ```python
  from django.db import models
  
  # Create your models here.
  class Movies(models.Model):
      title = models.CharField(max_length=20)
      title_en = models.CharField(max_length=20)
      audience = models.IntegerField()
      open_data = models.DateField()
      genre = models.CharField(max_length=20)
      watch_grade = models.CharField(max_length=20)
      score = models.FloatField()
      poster_url = models.TextField()
      description = models.TextField()
  
  class Comments(models.Model):
      movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='comments')
      content = models.CharField(max_length=40)
      score = models.IntegerField()
  ```


​
​
​
- forms.py
​
  
  ```python
  from django import forms
  from .models import Movies, Comments
  
  class MoviesForm(forms.ModelForm):
      title = forms.CharField(label='제목')
      title_en = forms.CharField(label='제목(영문)')
      audience = forms.IntegerField(label='누적관객수')
    open_data = forms.DateField(label='개봉일')
      genre = forms.CharField(label='장르')
      watch_grade = forms.CharField(label='관람등급')
      score = forms.FloatField(label='평점')
      poster_url = forms.CharField(label='포스터URL')
      description = forms.CharField(label='영화 소개', widget=forms.Textarea())
      class Meta:
          model = Movies
          fields = '__all__'
  
  
  class CommentForm(forms.ModelForm):
      content = forms.CharField(label='한줄평', widget=forms.TextInput())
      score = forms.IntegerField(label='평점')
      class Meta:
          model = Comments
          fields = ['content', 'score', ]
  ```
  
  

* views.py
​
  
  ```python
  from django.shortcuts import render, redirect, get_object_or_404
  from .models import Comments, Movies
  from .forms import CommentForm, MoviesForm
  from django.views.decorators.http import require_POST, require_GET
  
  @require_GET
  def index(request):
      movies = Movies.objects.all()
      return render(request, 'movies/index.html', {'movies': movies})
  
  
  def create(request):
      if request.method == 'POST':
          movie_form = MoviesForm(request.POST)
          if movie_form.is_valid():
              movie = movie_form.save()
              return redirect('movies:detail', movie.pk)
      else:
          movie_form = MoviesForm()
      return render(request, 'movies/create.html', {'movie_form':movie_form})
  
  
  @require_GET
  def detail(request, movie_pk):
      movie = get_object_or_404(Movies, pk=movie_pk)
      comment_form = CommentForm()
      return render(request, 'movies/detail.html', {'movie':movie, 'comment_form':comment_form})
  
  
  @require_POST
  def delete(request, movie_pk):
      movie = get_object_or_404(Movies, pk=movie_pk)
      movie.delete()
      return redirect('movies:index')
  
  
  def update(request, movie_pk):
      movie = get_object_or_404(Movies, pk=movie_pk)
      if request.method == 'POST':
          movie_form = MoviesForm(request.POST, instance=movie)
          if movie_form.is_valid():
              movie_form.save()
              return redirect('movies:detail', movie_pk)
      else:
          movie_form = MoviesForm(instance=movie)
      return render(request, 'movies/update.html', {'movie_form': movie_form, 'movie_pk':movie_pk})
      
  @require_POST
  def review(request, movie_pk):
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.movie_id = movie_pk
          comment_form.save()
      return redirect('movies:detail', movie_pk)
  
  @require_POST
  def comments_delete(request, movie_pk, comment_pk):
      comment = get_object_or_404(Comments, pk=comment_pk)
      comment.delete()
      return redirect('movies:detail', movie_pk)
  ```
  
  



​
- urls.py
​
  
  ```python
  from django.urls import path
  from . import views
  
  app_name = 'movies'
  
  urlpatterns = [
      path('', views.index, name='index'),
      path('<int:movie_pk>/', views.detail, name='detail'),
      path('create/', views.create, name='create'),
      path('<int:movie_pk>/update/', views.update, name='update'),
      path('<int:movie_pk>/delete/', views.delete, name='delete'),
      path('<int:movie_pk>/review/', views.review, name='review'),
      path('<int:movie_pk>/comments_delete/<int:comment_pk>', views.comments_delete, name='comments_delete'),
  ]
  ```
  



​
​
​
## 2. HTML

#### 주요 코드 내용

* index.html
​
  ```html
  {% extends 'base.html' %}
  
  {% block container %}
  {% load static %}
  <h1>영화 목록</h1>
  <div>
      <a href="{% url 'movies:create' %}">새 영화 등록</a>
  </div>
      <img src="{% static 'movies/image.jpg' %}"/>
  <ul>
      {% for movie in movies %}
      <li>
          <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a>
          <span>{{ movie.score }}</span>
      </li>
      {% empty %}
      <p>저장된 영화가 없습니다. 새 영화를 등록해주세요</p>
      {% endfor %}
  </ul>
  {% endblock container %}
  ```
  
  



​
- create.html
​
  
  ```html
  {% extends 'base.html' %}
  
  {% block container %}
  <h1>새 영화 등록</h1>
  
  <form method="post" action="{% url 'movies:create' %}">
      {% csrf_token %}
      {{ movie_form.as_p }}
      <input type="submit" value="등록"/>
  </form>
  {% endblock container %}
  ```
  



​
​
​
- detail.html
​
  
  ```html
  {% extends 'base.html' %}
  
  {% block container %}
  
  <h1>{{ movie.title }} : {{ movie.title_en }}</h1>
  <hr>
  <div>
      <div>누적관객수: {{ movie.audience }}</div>
      <div>개봉일: {{ movie.open_date }}</div>
      <div>장르: {{ movie.genre }}</div>
      <div>관람등급: {{ movie.watch_grade }}</div>
      <div>평점: {{ movie.score }}</div>
      <div>포스터이미지: {{ movie.poster_url }}</div>
  </div>
  <hr>
  <p>{{ article.description }} </p>
  <div>  
      <a href="{% url 'movies:index'%}">목록</a>  
      <a href="{% url 'movies:update' movie.pk %}">수정</a>  
      <form action="{% url 'movies:delete' movie.pk %}" method="post" style="display: inline-block;">
      {% csrf_token %}
      <input type="submit" value="삭제"/>
  </form> 
  </div>
  
  <ul>
      {% for comment in movie.comments.all %}
      <li>
          {{ comment.content }} : {{ comment.score }}
          <form action="{% url 'movies:comments_delete' movie.pk comment.pk %}" style="display: inline-block;" method="post">
              {% csrf_token %}
              <input type="submit" value="삭제"/>
          </form>
      </li>
      {% empty %}
      <p>한줄평이 없습니다. 평가해주세요.</p>
      {% endfor %}
  </ul>
  
  <form action="{% url 'movies:review' movie.pk %}" method="post">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit" value="작성"/>
  </form>
  
  {% endblock %}
  ```


​
​
​
- update.html
​
  
  ```html
  {% extends 'base.html' %}
  
  {% block container %}
  
  <h1>영화 정보 수정</h1>
  
  <form method="post" action="{% url 'movies:update' movie_pk %}">
      {% csrf_token %}
      {{ movie_form.as_p }}
      <input type="submit" value="수정"/>
  </form>
  {% endblock %}
  ```