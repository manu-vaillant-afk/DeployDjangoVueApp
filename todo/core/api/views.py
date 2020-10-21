from django.shortcuts import render

from rest_framework import generics

from todo.core.base.models import Todo
from .serializers import TodoSerializer


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
