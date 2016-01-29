from rest_framework import views as drf_views, viewsets, permissions, renderers
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, NotFound
from django.contrib.auth.models import User

from django.shortcuts import HttpResponse, render_to_response
from .models import Thread
from .serializers import ThreadSerializer, UserSerializer


class ThreadPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user in obj.participants.all():
            return True
        raise PermissionDenied({"message": "Permission denied"})



class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all().order_by('-last_message')
    serializer_class = ThreadSerializer
    permission_classes = (permissions.IsAdminUser, ThreadPermission, )

    def list(self, request, *args, **kwargs):
        threads = self.queryset.filter(participants = request.user)
        serializer = ThreadSerializer(threads, many=True, context={'request': request})
        return Response(serializer.data)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )


def index(request):
    context = {}
    return render_to_response('index.html', context)