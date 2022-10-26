from rest_framework import serializers

from ads.models.comment import Comment

from ads.models.ad import Ad
from users.models import User


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class CommentListSerializer(serializers.ModelSerializer):

    author_id = serializers.SlugRelatedField(
        source="author",
        required=False,
        many=False,
        queryset=User.objects.all(),
        slug_field='pk'
    )

    author_first_name = serializers.SlugRelatedField(
        source="author",
        required=False,
        many=False,
        queryset=User.objects.all(),
        slug_field='first_name'
    )

    author_last_name = serializers.SlugRelatedField(
        source="author",
        required=False,
        many=False,
        queryset=User.objects.all(),
        slug_field='last_name'
    )

    author_image = serializers.SerializerMethodField('get_author_image_url')

    ad_id = serializers.SlugRelatedField(
        source="ad",
        required=False,
        many=False,
        queryset=Ad.objects.all(),
        slug_field='pk'
    )

    class Meta:
        model = Comment
        fields = [
            "pk", "text", "author_id", "created_at",
            "author_first_name", "author_last_name", "ad_id", "author_image"]

    def get_author_image_url(self, obj):
        request = self.context.get("request")
        image_url = obj.author.image.url if obj.author.image else '/django_media/user_avatars/default_picture.jpg'
        return request.build_absolute_uri(image_url)


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ["text"]
