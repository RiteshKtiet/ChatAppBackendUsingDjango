from django.forms import ModelForm#this helps to create a form out of a model 
from .models import Room 

class RoomForm(ModelForm):
    class Meta:
        model= Room
        fields= '__all__'

