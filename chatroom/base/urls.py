from django.urls import path #getting path function 
from . import views #getting path functions 



#these will be the urls user can go to 
#the middile one in the each array element is the funciton which will run at each url route 
urlpatterns = [
    path('', views.home, name= "home"),
    path('room/<str:pk>', views.room, name="room" ),
    path('create-room/', views.createRoom,name="create-room"),
    path('update-room/<str:pk>/', views.updateroom,name="update-room")

]