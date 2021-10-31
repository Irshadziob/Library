from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django . contrib import messages,auth


# Create your views here.
from Bookapp.form import MovieForm
from Bookapp.models import Library


def home(request):
    obj=Library.objects.all()

    return render(request,'index.html',{'obj':obj})

def login(request):
    if request.method == 'POST' :
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')
    return render(request,'login.html')



def register(request):
    if request.method == 'POST' :
        username=request.POST['name']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if password == password1 :
            if User.objects.filter(username=username).exists():
                messages.info(request,"its already on db")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"its already on db email")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)

                user.save();
                return redirect('login')

        else:
            messages.info(request,"password incorrect")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def view(request,library_id):
    library = Library.objects.get(id=library_id)
    return render(request,'view.html',{'library':library})


def update(request,id):
    library = Library.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=library)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'update.html',{'form':form,'library':library})

def delete(request,id):
    if request.method == 'POST':
        library = Library.objects.get(id=id)
        library.delete()
        return redirect('/')
    return render(request,'delete.html')



def add_library(request):
    if request.method == "POST":
        name=request.POST.get('name')
        descreption=request.POST.get('descreption')
        year=request.POST.get('year')
        image=request.FILES['image']
        author=request.POST.get['author']
        library=Library(name=name,descreption=descreption,year=year,image=image,author=author)
        library.save()
    return render(request,'add.html')


