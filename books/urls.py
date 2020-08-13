from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from books import views

urlpatterns = [
    path('api/books', views.BookList.as_view()),
    path('api/books/<int:pk>/', views.BookDetail.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns)