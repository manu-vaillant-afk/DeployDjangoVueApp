from todo.core.base.models import Todo

from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("value", "checked")
