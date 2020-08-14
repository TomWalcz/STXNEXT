from rest_framework import mixins
from rest_framework import generics
from books.models import Book
from books.serializers import BookSerializer
# import django_filters.rest_framework
# import django_filters
from django_filters.rest_framework import DjangoFilterBackend

class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'authors']


class BookDetail(generics.RetrieveAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
