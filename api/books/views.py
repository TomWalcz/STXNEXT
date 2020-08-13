from rest_framework import mixins
from rest_framework import generics
from books.models import Book
from books.serializers import BookSerializer
from rest_framework import filters
from django_filters import rest_framework as filters

class BookList(generics.ListAPIView):

    def get_queryset(self):
        
        queryset = Book.objects.all()
        title = self.request.query_params.get('title')
        authors = self.request.query_params.get('authors')
        if title:
            queryset = queryset.filter(title__title=title)
        if authors:
            queryset = queryset.filter(books__authors=authors)
        return queryset
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
        
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

class BookDetail(generics.RetrieveAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
