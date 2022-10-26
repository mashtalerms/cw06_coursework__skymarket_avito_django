from rest_framework.viewsets import ModelViewSet

from ads.models.comment import Comment
from ads.serializers.comment import CommentListSerializer

from ads.serializers.comment import CommentCreateSerializer


from ads.models.ad import Ad

from ads.serializers.comment import CommentSerializer

from ads.permissions import GeneralPermission


class CommentViewSet(ModelViewSet):
    """Comment View Set for whole CRUD"""
    serializer_class = CommentSerializer
    permission_classes = (GeneralPermission,)

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.kwargs["ad_id"])

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return CommentListSerializer

        if self.action == "create" or self.action == "partial_update":
            return CommentCreateSerializer

        return super().get_serializer_class()

    def perform_create(self, serializer):
        ad = Ad.objects.get(pk=self.kwargs["ad_id"])
        serializer.save(author=self.request.user, ad=ad)
