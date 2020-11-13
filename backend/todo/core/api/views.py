from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from .permissions import IsOwnerOrNothing
from todo.core.base.models import Todo
from .serializers import TodoSerializer
from django.conf.urls import url


class TodoList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Todo.objects.none()
        return Todo.objects.filter(owner=user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrNothing]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'uuid'




