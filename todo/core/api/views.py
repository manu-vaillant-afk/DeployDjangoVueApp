from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from .permissions import IsOwnerOrNothing
from todo.core.base.models import Todo
from .serializers import TodoSerializer
from django.conf.urls import url


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrNothing]
    # def get_queryset(self):
    #     user = self.request.user
    #     return user.todos.all()

    

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrNothing]



