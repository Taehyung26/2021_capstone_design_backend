from django.contrib import admin
from django.urls import path
from rest_framework.schemas.inspectors import ViewInspector
from parkMoaApp import views  

urlpatterns = [
    path('', views.SearchView.as_view()),  
    # path('parkinfo/<>', views.SearchView.as_view()),
]
