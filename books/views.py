from rest_framework import generics
from books.models import Book
from rest_framework.response import Response
from books.serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

class BookList(generics.ListCreateAPIView):

    # List all books, create new instance

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    # renderer_classes = [JSONRenderer]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'authors', 'publishedDate']

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(generics.RetrieveAPIView):


    # Retrieve books instance

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

        