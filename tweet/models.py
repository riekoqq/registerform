from django.db import models

# Create your models here.
class Tweets():
    content = models.TextField()
    time = models.DateTimeField()
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.content
