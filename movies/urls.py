from django.contrib import admin
from django.urls import path
from movies.views import MovieView, SearchView

urlpatterns = [
    path('', MovieView.as_view()),
    path('<int:pk>', MovieView.as_view()),
    path('search', SearchView.as_view())
]
