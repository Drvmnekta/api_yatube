"""Module with serializers."""

from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from yatube_api.posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    """Serializer of post model."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        """Meta class of serializer."""

        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Serializer of comment model."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        """Meta class of serializer."""

        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    """Serializer of group model."""

    class Meta:
        """Meta class of serializer."""

        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    """Serializer of follow model."""

    user = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all()
    )

    class Meta:
        """Meta class of serializer."""

        model = Follow
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            )
        ]

    def validate_following(self, value: str) -> str:
        """Validate following field.
        
        Args:
            value: slug of following field to validate.
        
        Returns:
            validated field.
        
        Raises:
            ValidationError if value is invalid.
        """
        user = self.context.get('request').user
        author = get_object_or_404(User, username=value)
        if author == user or author is None:
            raise serializers.ValidationError('Самоподписки запрещены')
        return value
