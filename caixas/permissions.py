from rest_framework import permissions
from caixas.models import Caixa

from rest_framework.views import Request, View



class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj:Caixa):
        return  request.user == obj.user 

