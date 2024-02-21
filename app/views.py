from django.shortcuts import render,redirect
from .models import *

loggedin = False
curr_user = ''

# Create your views here.
def index(request):
    return render(request,'login.html')

def home(request):
    if(loggedin==True):
        redirect('/dashboard')
    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        name = request.POST.get('name')
        password = request.POST.get('pass')
        pass2 = request.POST.get('pass2')

        if(password==pass2):
            user = User(username=name,password=password)
            user.save()
            return redirect('/home')
    return render(request,'signup.html')

def login(request):
    global curr_user,loggedin
    if request.method=="POST":
        name = request.POST.get('name')
        password = request.POST.get('pass')

        if(name == "admin" and password == "123"):
            loggedin=True
            curr_user = 'admin'
            return redirect('/admin')

        if User.objects.filter(username=name).exists():
            l = User.objects.filter(username=name).values_list()
            print(l)
            if l[0][2] == password:
                print('double yes')
                loggedin = True 
                curr_user=l[0][1]
                return redirect('/dashboard')
            else:
                return redirect('/home')


def dashboard(request):
    global curr_user
    if(loggedin==False):
        redirect('/login')
    books = Book.objects.all().values()
    context = {
        'books':books,
        'curr_user':curr_user,
    }
    return render(request,'dashboard.html',context)

def admin(request):
    if(loggedin==False):
        redirect('/home')
    return render(request,'admin.html')

def logout(request):
    global loggedin
    loggedin=False
    return redirect('/home')

def addbooks(request):
    if request.method=="POST":
        name = request.POST.get('name')
        image = request.POST.get('image')
        author = request.POST.get('author')

        boo  = Book(name=name,author=author,picture=image)
        boo.save()
        return redirect('/admin')
    

def search(request):
    global curr_user
    if request.method=="POST":  
        search = request.POST.get('search')
        
        items1 = Book.objects.filter(name__icontains=search).values_list()
        items2 = Book.objects.filter(name__icontains=search).values_list()
        items3 = Book.objects.filter(name__icontains=search).values_list()

        values = []
        for i in items1[0]:
            if i[1] not in values:
                values.append(i)
        for i in items2[0]:
            if i[1] not in values:
                values.append(i)
        for i in items3[0]:
            if i[1] not in values:
                values.append(i)

        print(values)

        context = {
            'curr_user':curr_user,
            'name':values,
        }

        return render(request,'searched.html',context)