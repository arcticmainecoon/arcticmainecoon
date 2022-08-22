from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=120)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        x = self
        y = self.id
        return F"Blog #{y}, titled: {x.title} "
