from rest_framework import serializers
from favourite.api.models import Favourite




class FavouriteListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    book = serializers.SerializerMethodField()
   
    def get_user(self, obj):
       return obj.user.username

    def get_book(self, obj):
        return obj.book.title
    
    class Meta:
        model = Favourite
        fields = ['pk', 'user', 'book']
        
class FavouriteCreateSerializer(serializers.ModelSerializer):
    def get_serializer_context(self):
        return {'request': self.request}
    
    
    def validate(self, attrs):
        user = self.context['request'].user
        queryset = Favourite.objects.filter(user = attrs['user'], book= attrs['book'])
        if not user.is_superuser and attrs['user'] != user:
            raise serializers.ValidationError('You can not add favourite book to another profile')
        
        if queryset.exists():
            raise serializers.ValidationError("You already favourited this book to this profile")
        return attrs
    
    class Meta:
        model = Favourite
        fields = '__all__'
        