from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    STATUS_CHOISES = [
        ('todo','Треба виконати'),
        ('in_progress','Виконується'),
        ('done','Виконано'),
    ]
    PRIORITY_CHOISES = [
        ('low','низький'),
        ('middle','Середній'),
        ('hight','Високий'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOISES,default='todo')
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOISES,default='middle')

    deadline = models.DateTimeField(null=True,  blank=True)
    created =  models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
