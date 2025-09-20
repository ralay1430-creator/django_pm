from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class projectStatus (models.IntegerChoices):
    PENDING = 1 , "pending"
    COMPLETED = 2 , "completed"
    POSTPONED = 3 , "postponde"
    CANCELED = 4, "cancleed"




class project (models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField ()
    status = models.IntegerChoices(
        choices = projectStatus.choices ,
        default = projectStatus.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    Category = models.ForeignKey(Category , on_delete=models.PROTECT)
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
         return   self.title

class Task (models.Model):
    descriptoion = models.TextField()
    is_conpleted = models.BooleanField(default=False)
    project = models.ForeignKey(project ,on_delete=models.CASCADE )

    def __str__ (self):
        return self.descriptoion