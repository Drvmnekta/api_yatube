"""Module with permissions."""

from rest_framework import permissions


class AuthorOrReadOnlyPermission(permissions.BasePermission):
    """Author or read only permission.
    
    Return true if user is author, else forbidden.
    """

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class FollowerPermission(permissions.BasePermission):
    """Permission for followers.
    
    Return true if user is a follower, else forbidden.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.user == request.user)
