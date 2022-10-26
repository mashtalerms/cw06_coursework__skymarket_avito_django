# from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, status
from ads.models.ad import Ad
from ads.serializers.ad import AdSerializer
from ads.serializers.ad import AdCreateSerializer
from ads.serializers.ad import AdListSerializer
from ads.serializers.ad import AdRetrieveSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from ads.permissions import GeneralPermission
from rest_framework.viewsets import ModelViewSet


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (GeneralPermission,)

    def get_serializer_class(self):
        if self.action == "list":
            return AdListSerializer

        if self.action == "retrieve":
            return AdRetrieveSerializer

        if self.action == "create" or self.action == "partial_update":
            return AdCreateSerializer

        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['GET'], url_path=r'me', name='Get own ads')
    def users_ads(self, request, *args, **kwargs):

        user = request.user
        user_ads = Ad.objects.filter(author_id__exact=user.id)
        page = self.paginate_queryset(user_ads)

        if page is not None:
            serializer = AdListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AdListSerializer(self.queryset, many=True)
        return Response(serializer.data)
