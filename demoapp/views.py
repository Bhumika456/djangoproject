
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Contact
from .models import Books, Student
from .forms import BookForm, StudentForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
import csv
# Create your views here.
        
def home(request):
    if request.method=='POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        url=fs.url(myfile)
        print('save')
        #context['url']=fs.url(filename)


    #return render(request,'index.html',context)
    dict={'name':'pride','id':101}
    return render(request,'index.html',dict)
    

def test(request):
    form=""
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()        
            print('Save')         
    return render(request,'test.html',{'form':form})

    #return HttpResponse("<h1 align='center'><font color='red' face='algerian'>Welcome to Django</h1>")
    #return HttpResponse("<script>alert('welcome to javascript tag');</script>")
    
def contact(request):

    if request.method=="POST":
        uname=request.POST['ename'];
        uemail=request.POST['Email'];

        con=Contact(name=uname,email=uemail)
        con.save()
        print('save successfully')
    records=Contact.objects.all()    
    d={'records':records}

    #print(uname,uemail)
    return render(request,'contact.html',d)

def about(request):
    return HttpResponse('about page')

#def contact(request):
    #return render(request,'contact.html')   

def add(request):
    a=int(request.POST['num1'])
    b=int(request.POST['num2'])

    c=a+b
    return render(request,'result.html',{'sum':c}) 
       
def upload_book(request):
    if request.method=="POST":
        form=BookForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            print('save')
            return redirect('book_list')
    else:
        form=BookForm()
    
    return render(request,'upload_book.html',{'book':form})    

def book_list(request):
    b=Books.objects.all()
    return render(request,'book_list.html',{'books':b})    


def delete_book(request,pk):
    if request.method=='POST':
        book=Books.objects.get(pk=pk)
        book.delete()
    return redirect('book_list') 


def send_email(request):
    if request.method=='POST':
        message=request.POST['message']
        send_mail('Testing',message,settings.EMAIL_HOST_USER,['bhumikasuri335@gmail.com'],fail_silently=False)
    return render(request,'send_email.html')       


def ssession(request):
    request.session['ename']='Mehaan'
    request.session['email']='Mehaan@gmail.com'
    return HttpResponse("Session are set")


def gsession(request):
    name=request.session['ename']
    email=request.session['email']
    return HttpResponse(name)

def scookie(request):
    response=HttpResponse("cookie are set")    
    response.set_cookie('user','pride')
    return response


def gcookie(request):
    name=request.COOKIES['user']
    return HttpResponse(name)


def csvs(request):
    response=HttpResponse(content_type='text/csv')   
    response['Content-Disposition'] ='attachment; filename="file.csv"'
    st=Student.objects.all()
    writer=csv.writer(response)
    for s in st:
        writer.writerow([s.name,s.email,s.mobile])
    return response    



