from rest_framework import serializers
from khata.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'phone', 'price', 'address', 'year', 'area', 'author', 'excerpt', 'content', 'status')
        model = Post