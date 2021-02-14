from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
import omdb
from .models import Favorite

API_KEY = '2e89eb0c'
omdb.set_default('apikey', API_KEY)
omdb.set_default('tomatoes', True)

# Create your views here.
@login_required
def index(request):
    movies = omdb.search_movie('true')

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
           movies = movie_api(form)
    else:
        form = SearchForm()
    return render(request,'index.html', {'form': form, 'movies': movies })


def movie_api(form):
    title = form.cleaned_data['title']
    year = form.cleaned_data['year']
    genre = form.cleaned_data['genre']

    if title:
        if year:
            movie = []
            movie.append(omdb.get(title=title, year=year))
            return movie
        else:
            return omdb.search_movie(title)


@login_required
def single_movie(request, id):
    movie = omdb.imdbid(id)
    return render(request,'search/single_movie.html', {'movie': movie })


def make_favorite(request, id):
    fev = Favorite.objects.filter(user=request.user, movie=id)
    if fev:
        return HttpResponseRedirect(reverse('index'))
    q = Favorite(user=request.user, movie=id)
    q.save()
    return HttpResponseRedirect(reverse('favorite'))


def remove_favorite(request, id):
    q = Favorite.objects.get(user=request.user, movie=id)
    q.delete()
    return HttpResponseRedirect(reverse('favorite'))


@login_required
def favorite(request):
    fev = Favorite.objects.filter(user=request.user)
    movies = []
    for fev in fev:
        movies.append(omdb.imdbid(fev.movie))
    return render(request,'search/favorite.html', {'movies': movies } )
