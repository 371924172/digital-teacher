from rest_framework.permissions import BasePermission
from .models import Role


# 自定义权限管理
class isAdmin(BasePermission):
    def has_permission(self, request, view):
        # 获取当前登陆用户
        user = request.user
        role = Role.objects.filter(user_id=user.id)
        roles = []
        for r in role:
            if r.name == 'admin':
                return 1
        return bool(user.is_superuser)


# 重写jwt的登录视图的构造相应数据函数，追加userid和username
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'userid': user.id,
        'status': user.status
    }
