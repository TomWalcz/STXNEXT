from django.urls import path
from api import views

urlpatterns = [
    path('api/', views.book_list),
    path('api/<int:pk>/', views.book_detail)
]
