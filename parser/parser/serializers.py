from datetime import datetime
from rest_framework import serializers

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()
        comment = Comment(email='leila@example.com', content='foo bar')


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


Account = serializers.CharField()
Album = serializers.CharField()
AlbumSerializer = serializers.CharField()

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created']
        read_only_fields = ['account_name']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.SlugRelatedField(
    many=True,
    read_only=True,
    slug_field='title'
    )
    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']
        qs = Album.objects.all()
        print(AlbumSerializer(qs, many=True).data)

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']
        def __str__(self):
            return '%d: %s' % (self.order, self.title)

