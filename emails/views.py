from django.shortcuts import render, redirect ,HttpResponse , HttpResponseRedirect ,get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.mail import send_mail , BadHeaderError
from django.core.mail import EmailMessage
from django.contrib.auth.models import User , auth
from .forms import UserRegistrationForm , DocumentForm , DataLoadForm , addForm
from django.contrib.auth.decorators import login_required
from . models import Document
import pandas as pd
import openpyxl 
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

import boto3
import re


ses = boto3.client('ses')
s3 = boto3.client('s3')

# Create your views here.

def home(request):
    return render(request,'home.html')

@login_required()

def login(request):
    user=User.objects.all()
    response=ses.verify_email_address(EmailAddress='request.user.email')
    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save()
            print(email)
            messages.success(request, f'Your account has been created. You can log in now and verify your email link!')
            # verify_email(email)    
            custom_email_verify(email)
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


@login_required()
def vendor(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user= request.user
            form.save()
            # return HttpResponse("File uploaded ")
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'vendor.html', {'form': form})


# @login_required()
def clean_data(request,id):
    
    doc = Document.objects.get(id=id).document
    df = pd.read_excel (r'doc')
    data = df.drop_duplicates()
    edata = data.values.tolist()
    EMAIL_HOST_USER = 'request.user.email'
    for i in edata:
        print(i)
        message = "<html><h1>Hello , We are Providing an Offer For you ,please register with us get leads to your business</h1><a href='unsubscribe'>UnSubscribe</a></html>"
        if i :
            msg=EmailMessage('subject',message,request.user.email,i)
            msg.content_subtype = "html"  
            msg.send()
        else:
            return HttpResponseRedirect('register/')
    return redirect('clean/')



def clean(request,id):
    doc=Document.objects.get(id=id)
    return render(request,'clean.html',{'doc':doc})   

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')



def unsubscribe(id):
    doc = Document.objects.all()
    for i in doc :
        print(i.id)
        if i.id :
            Document.objects.filter(id = id).delete()
        else:
            print("Not authorised")
# unsubscribe(37)


@login_required()
def excel_data(request):
    user = User.objects.all()
    doc = Document.objects.all()
    return render(request, 'excel.html', {'doc': doc})
        


@login_required()
def add(request,id):
    if request.method == 'POST' :
        form = addForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email',' ')
            doc= Document.objects.get(id=id).document
            wb =openpyxl.load_workbook(doc)
            ws = wb.active
            ws.append([email])
            wb.save('doc')
            message = "<html><h1>Hello , We are Providing an Offer For you ,please register with us get leads to your business</h1><a href='unsubscribe'>UnSubscribe</a></html>"
            msg=EmailMessage('subject',message,request.user.email,[email])
            msg.content_subtype = "html"  
            msg.send()
                
            return render(request,'eview.html',{'email':email})
    else:
        form = addForm()
    return render(request,'add.html',{'form':form})




    



    




def unsubscribe(id):
    doc=Document.objects.get(id=id).document
    print(doc)
    df = pd.read_excel(r'doc')
    print(df)
    # d = df.drop("email")
    # print(d)
    
# unsubscribe(41)    



       




        

            

@login_required()
def eview(request,id):
    # regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    doc = Document.objects.get(id=id).document
    df = pd.read_excel(doc)
    # print(df.to_string(index=False))
    df = df.drop_duplicates(keep = False)
    # print(df.to_string(index=False))
    df = df.dropna()
    print(df)
    x = df.to_string(index=False)
    # print(x)
    email = re.findall('\S+@\S+', x)   
    # print(lst)
    for i in email :
        message = "<html><h1>Hello , We are Providing an Offer For you ,please register with us get leads to your business</h1><a href='unsubscribe'>UnSubscribe</a></html>"
        msg=EmailMessage('subject',message,request.user.email,[i])
        msg.content_subtype = "html"  
        msg.send()
    return render(request,'eview.html',{'email':email})
