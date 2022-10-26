from datetime import datetime

from rest_framework import serializers

from ads.models.ad import Ad
from users.models import User
from users.serializers import CurrentUserSerializer


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = "__all__"


class AdListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description"]


class AdRetrieveSerializer(serializers.ModelSerializer):

    phone = serializers.SlugRelatedField(
        source="author",
        required=False,
        many=False,
        queryset=User.objects.all(),
        slug_field='phone'
    )

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

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price",
                  "phone", "description", "author_first_name", "author_last_name", "author_id"]


class AdCreateSerializer(serializers.ModelSerializer):

    phone = serializers.SlugRelatedField(
        source="author",
        required=False,
        many=False,
        queryset=User.objects.all(),
        slug_field='phone'
    )

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

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price",
                  "phone", "description", "author_first_name", "author_last_name", "author_id"]
