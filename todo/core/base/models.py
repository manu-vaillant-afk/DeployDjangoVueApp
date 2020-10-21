from django.db import models


class Todo(models.Model):
    value = models.TextField()
    checked = models.BooleanField(default=False)

    def __str__(self):
        if not self.checked:
            c = "☐"
        else:
            c = "☑"

        return f"{c} {self.value}"
