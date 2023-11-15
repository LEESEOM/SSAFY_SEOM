from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    
    username = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Article
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)