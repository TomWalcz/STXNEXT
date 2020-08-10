from rest_framework import serializers
from api.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'publishedDate']
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(allow_blank=True, max_length=100)
    # authors= serializers.CharField(allow_blank=True, max_length=100)
    # publishedDate = serializers.PositiveIntegerField()

    # def create(self, validated_data):

    #     return Book.objects.create(**validated_data)

    # def update(self, instance, validated_data):

    #     instance.title = validated_data.get('title', instance.title)
    #     instance.authors = validated_date.get('authors', instance.authors)
    #     instance.publishedDate = validated_date.get('publishedDate', instance.publishedDate)
    #     instance.save()
    #     return instance