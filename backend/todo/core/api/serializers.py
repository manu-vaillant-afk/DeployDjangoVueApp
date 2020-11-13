from todo.core.base.models import Todo, MyUser

from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        # fields = ("id" ,"value", "checked", "owner")
        fields = ("uuid" ,"value", "checked", "owner")

            
