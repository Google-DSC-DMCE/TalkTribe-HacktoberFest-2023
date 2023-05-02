from django.shortcuts import render,redirect #NOTE for templates
from django.contrib import messages
from django.contrib import auth #NOTE for autharisation
from django.db.models import Q 
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import *

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        # checking if user with that username exist::
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')
        # checking if user with that username has that password::
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,'username or password is incorrect')
    context = {
        "page" : "login"
    }
    return render(request,'base/login_register.html',context)

def logoutUser(request):
    print(request.user)
    auth.logout(request)
    return redirect('home')

def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False) 
            user.username = user.username.lower()
            user.save()
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Error occured during registeration')
    form = UserCreationForm()
    
    context = {
        "page":"register",
        'form':form
    }
    return render(request,'base/login_register.html',context)
    

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q),
        Q(description__icontains = q),
        Q(name__icontains = q)
    )
    topics = Topic.objects.all()
    room_message = Message.objects.filter(
        Q(room__topic__name__icontains=q)
    )
    context = {
        'room_count':rooms.count(),
        'rooms':rooms,
        'topics':topics,
        'room_message':room_message,
    }
    return render(request,'base/home.html',context)

def user(request,pk):
    user = User.objects.get(id=pk)
    topics = Topic.objects.all()
    rooms = user.room_set.all()
    room_message = user.message_set.all()
    context = {
        'user':user,
        'rooms':rooms,
        'topics':topics,
        'room_message':room_message,
    }
    return render(request,'base/user_page.html',context)

def room(req,primarykey):
    room = Room.objects.get(id=primarykey)
    if req.method == 'POST':
        message= Message.objects.create(
            user=req.user,
            room=room,
            body=req.POST.get('message'),
        )
        room.participants.add(req.user)
        return redirect('room',primarykey)
    room_messages = room.message_set.all().order_by('-created')  
    participents = room.participants.all()
    context = {
        'room' : room,
        'room_messages':room_messages,
        'participants':participents
    }
    return render(req,'base/room.html',context)
# Create your views here.

@login_required(login_url="login")
def delete_message(request,pk):
    message = Message.objects.get(id=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('home')
        
    return render(request,'base/delete.html',{'obj' : message})

@login_required(login_url="login")
def create_room(req):       
    form = RoomForm()
    if req.method == "POST":
        form = RoomForm(req.POST)
        if form.is_valid():
            print(f"form = {form}")
            form.save()
            return redirect('home')
        
    context = {
        'form' : form
    }
    return render(req,'base/room_form.html',context) 

@login_required(login_url="login")
def update_room(req,pk):
    room = Room.objects.get(id = pk)
    if req.user == room.host:
        form = RoomForm(instance=room)
        if req.method == 'POST':
            form = RoomForm(req.POST,instance=room)
            if form.is_valid():
                form.save()
                return redirect('home')
        context={
            'form' : form
        }
        return render(req,'base/room_form.html',context)
    else: 
        return HttpResponse('Unautharized to change the room')

@login_required(login_url="login")
def delete_room(req,pk):
    room = Room.objects.get(id=pk)
    if req.method == 'POST':
        room.delete()
        return redirect('home')
        
    return render(req,'base/delete.html',{'obj' : room})