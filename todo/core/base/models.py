from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
import uuid

class MyUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # todos = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name="owner")

    def __str__(self):
        return self.username

class Todo(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    value = models.TextField()
    checked = models.BooleanField(default=False)
    owner = models.ForeignKey(MyUser, related_name='todos', on_delete=models.CASCADE)

    class Meta:
            unique_together = [("value", "owner")]

    def __str__(self):
        if not self.checked:
            c = "☐"
        else:
            c = "☑"

        return f"{c} {self.value} uid:{self.uid}"



