from rest_framework import serializers
from book.api.models import Book

class BookSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='book:detail',
        lookup_field='slug'
    )

    username = serializers.SerializerMethodField()
    
    def get_username(self, obj):
        return str(obj.user.username)
    
    class Meta:
        model = Book
        fields = ['pk', 'title', 'content', 'image', 'slug', 'url', 'username']

class BookUpdateDeleteSerializer(serializers.ModelSerializer):
        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.content = validated_data.get('content', instance.content)
            instance.save()
            return instance

        def validate(self, attrs):
            if attrs["title"] == "forbidden-word":
                raise serializers.ValidationError("This title is not allowed to create or update.")
            return attrs

        class Meta:
            model = Book
            fields = ['title', 'content']

class BookCreateSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if attrs["title"] == "forbidden-word":
            raise serializers.ValidationError("This title is not allowed to create or update.")
        return attrs

    class Meta:
        model = Book
        fields = ['title', 'content', 'image']
        