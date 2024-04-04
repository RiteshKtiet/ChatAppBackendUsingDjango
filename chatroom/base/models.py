from django.db import models
from django.contrib.auth.models import User 
from django.db.models.deletion import CASCADE

# Create your models here.

class Topic(models.Model):
    name= models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host= models.ForeignKey(User, on_delete=models.SET_NULL, null= True )
    topic=models.ForeignKey(Topic, on_delete= models.SET_NULL, null=True)
    name=models.CharField(max_length= 200)
    description= models.TextField(null=True,blank= True)#this means null value allowed... null is for the database and blank for the form
    #participants
    updated= models.DateTimeField(auto_now=True)#to get time stamp when the table was updated i.e the toom info 
    created = models.DateTimeField(auto_now_add=True)#to get when it was creeated... auto now add doesnt change with each save
    class Meta:
        ordering=['-updated','-created']
    def __str__(self):
        return str(self.name) 
    
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete= models.CASCADE)
    BODY= models.TextField
    updated= models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body(0)