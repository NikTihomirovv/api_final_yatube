from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router_v1 = SimpleRouter()
router_v1.register('v1/posts', PostViewSet, basename='posts')
router_v1.register('v1/groups', GroupViewSet, basename='groups')
router_v1.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
router_v1.register('v1/follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
