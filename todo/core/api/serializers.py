from todo.core.base.models import Todo, MyUser

from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id" ,"value", "checked", "owner")

            
