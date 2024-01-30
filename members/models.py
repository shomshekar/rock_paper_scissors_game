from django.db import models

# Create your models here.

class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True, blank=True)

    # def __str__(self):
    #     return f"{self.firstname} {self.lastname}"
    

class GameResult(models.Model):
    member_id = models.ForeignKey(Members, on_delete=models.CASCADE)
    member_selection = models.CharField(max_length=255)
    computer_selection = models.CharField(max_length=255)
    result = models.TextField()
    created_datetime = models.DateTimeField(auto_now=True)