from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room 
from .forms import RoomForm 
# Create your views here.


# rooms = [
#     {'id':1, 'name':'lets learn pyhton'},
#     {'id':2, 'name':'lets learn java'},
#     {'id':3, 'name':'lets learn cpp'},
# ]
def home(request):
    rooms = Room.objects.all()
    context= {"rooms":rooms}
    return render(request,'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context= {"roomo":room}

    return render(request, 'base/roomi.html',context) 

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form= RoomForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('home')

    context ={'form':form}
    return render(request, 'base/room_form.html',context)


def updateroom(request,pk):
    room= Room.objects.get(id=pk)
    form= RoomForm(instance=room)
    context={'form': form }
    if request.method== 'POST':
        form= RoomForm(request.POST, insatnce=room )
        if form.is_valid():
            form.save()
            return redirect('home')


    return render(request, 'base/room_from.html',context)

    