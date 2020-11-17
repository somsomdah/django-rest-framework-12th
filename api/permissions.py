from rest_framework import permissions
from django.contrib.auth import get_user_model

from rest_framework import permissions

#
class IsSuperUserOrReadOnly(permissions.BasePermission):

    # 인증된 유저에 대해 접근 허용
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(slef, request, views, obj):
        # 조회 요청은 항상 True
        if request.method in permissions.SAFE_METHODS:
            return True
        # PUT, DELETE 요청에 한해 SuperUser에게만 허용
        return request.user.is_superuser


class IsUserOrSuperUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # 조회 요청은 해당 유저만 가능
        if request.method in permissions.SAFE_METHODS:
            if hasattr(obj,"profile"):
                return obj.profile==request.user
            elif hasattr(obj,"student"):
                return obj.student == request.user
            else:
                return False

        # PUT, DELETE 요청에 한해 SuperUser에게만 허용
        return request.user.is_superuser




