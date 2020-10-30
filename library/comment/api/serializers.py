from rest_framework import serializers 


from comment.api.models import Comment
from django.contrib.auth.models import User


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['createdAt',]
    
    def validate(self, attrs):
        if(attrs['parent']):
            if(attrs['parent'].book != attrs['book']):
                raise serializers.ValidationError('Comment s parent s post must be same with comment s post')
        return attrs 
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
class CommentListSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = '__all__'
        

    def get_replies(self, obj):
        if obj.any_children:
            return CommentChildSerializer(obj.children(), many=True).data
    
    
    
        
    
class CommentChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        

class CommentDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']