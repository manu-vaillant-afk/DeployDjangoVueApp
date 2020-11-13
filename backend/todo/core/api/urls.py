from django.contrib import admin
from django.urls import path
from .views import TodoList, TodoDetail
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path("todos/", TodoList.as_view(), name="todo_list"),
    path("todos/<uuid:uuid>/", TodoDetail.as_view(), name="todo_detail"),
    url(r'^$', schema_view),
]
