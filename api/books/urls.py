from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from books import views

urlpatterns = [
    path('api/v1/books', views.BookList.as_view()),
    path('api/v1/books/<int:pk>/', views.BookDetail.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns)