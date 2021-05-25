from rest_framework import serializers
from khata.models import Post
from users.models import NewUser



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'image', 'phone', 'price', 'address', 'slug', 'category', 'area', 'author', 'excerpt', 'content', 'status')
        model = Post


