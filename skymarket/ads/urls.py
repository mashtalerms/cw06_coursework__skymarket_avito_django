from django.urls import path, include
from rest_framework import routers

from ads.views.comment import CommentViewSet
from ads.views.ad import AdViewSet

ad_router = routers.SimpleRouter()
ad_router.register("ads", AdViewSet)
ad_router.register("ads/(?P<ad_id>[^/.]+)/comments", CommentViewSet, basename='comments')


urlpatterns = [
    path("", include(ad_router.urls)),
]
