from django.contrib import admin
from django.urls import path
from movies.views import MovieView

urlpatterns = [
    path('', MovieView.as_view()),
    path('<int:pk>', MovieView.as_view()),
]
