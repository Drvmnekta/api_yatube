"""Module with views."""

from django.db.models.query import QuerySet
from rest_framework import filters, mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from yatube_api.api.permissions import (AuthorOrReadOnlyPermission,
                                        FollowerPermission)
from yatube_api.api.serializers import (CommentSerializer, FollowSerializer,
                                        GroupSerializer, PostSerializer)
from yatube_api.posts.models import Group, Post


class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                viewsets.GenericViewSet):
    """Mixin viewset for create and list methods."""

    pass


class PostViewSet(viewsets.ModelViewSet):
    """Viewset for posts."""

    permission_classes = [AuthorOrReadOnlyPermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer: PostSerializer) -> None:
        """Create post object.
        
        Args:
            serializer: serializer object with data for post creation.
        """
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset for groups."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Viewset for comments."""

    permission_classes = [AuthorOrReadOnlyPermission]
    serializer_class = CommentSerializer

    def perform_create(self, serializer: CommentSerializer) -> None:
        """Create comment object.
        
        Args:
            serializer: serializer object with data for comment creation.
        """
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self) -> QuerySet:
        """Get queryset for viewset.
        
        Returns:
            queryset of comments.
        """
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        comments_queryset = post.comments.all()
        return comments_queryset


class FollowViewSet(CreateListRetrieveViewSet):
    """Viewset for follow objects."""

    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, FollowerPermission]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self) -> QuerySet:
        """Get queryset for viewset.
        
        Returns:
            queryset of comments.
        """
        return self.request.user.follower.all()
