from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, CommentViewSet, FollowList, GroupViewSet


router_v1 = SimpleRouter()
router_v1.register(r'posts', PostViewSet, basename='posts-list')
router_v1.register(r'^posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments-list')
router_v1.register(r'^posts/(?P<post_id>\d+)/comments/(?P<id>\d+)',
                   CommentViewSet, basename='comment-detail')
router_v1.register(r'follow', FollowList, basename='follow-list')
router_v1.register(r'groups', GroupViewSet, 'group-detail')

urlpatterns = [
    path('v1/', include(router_v1.urls))
]
