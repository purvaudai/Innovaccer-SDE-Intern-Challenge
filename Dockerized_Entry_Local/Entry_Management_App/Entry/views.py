from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import host, visitor, visit
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.conf import settings
from datetime import date
from django.core.mail import send_mail
from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
#account_sid='AC8e3ab6d3d8f5e153df216e32442dfda1'
auth_token = os.environ['TWILIO_AUTH_TOKEN']
#auth_token='cdea2c191b88831c9d7725a49fe50712'
client = Client(account_sid, auth_token)

# Create your views here.
def home(request):
    return render(request, 'home.html')

def host(request):
    return HttpResponse('host site')

def register(request):
    if(request.method=='POST'):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['email']
        email=username
        password1=request.POST['password1']
        password2=request.POST['password2']
        phone=request.POST['phone']
        try:
            validate_email(username)
        except ValidationError as e:
            messages.info(request, 'email is not valid')
            return redirect('register')
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, password=password1, email=email,first_name=first_name, last_name=last_name)
                user.save()
                #user2=User.objects.get(username=username)
                #user2_id=user2.id
                host2=host(user=user, phone=phone,)
                host2.save()
                print("user created")
                return redirect('/')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')
    else:
        return render(request, 'signup.html')

def checkin(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        hostemail=request.POST['h-email']
        checkin=request.POST['checkin']
        tentcheckout=request.POST['tentcheckout']
        address=request.POST['address']
        datenow=date.today()
        checkin2=str(datenow)+" "+checkin
        tentcheckout2=str(datenow)+" "+tentcheckout
        if User.objects.filter(email=hostemail).exists():
            v=visitor(name=name, email=email, phone=phone)
            try:
                v.save()
            except ValueError as e:
                messages.info(request, 'Phone Number is not valid, please include country code')
                return redirect('checkin')
            v.save()
            temph=User.objects.get(email=hostemail)
            #hh=host.objects.get(host=temph)
            hh=temph.host
            m=visit(timein=checkin2, tenttimeout=tentcheckout2, visitor=v, host=hh, address=address)
            m.save()
            subject='You have a Visitor: '+name
            message="You have an appointment with "+name+" at "+checkin2+"\nEmail ID: "+email+"\nPhone No.: "+str(phone)+"\n Tentative Check-out: "+tentcheckout2+"\nLocation: "+address
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[hostemail,]
            send_mail(subject, message, email_from, recipient_list)
            message = client.messages \
                .create(
                     body="You have an appointment with "+name+" at "+checkin2+"\nEmail ID: "+email+"\nPhone No.: "+str(phone)+"\nLocation: "+address,
                     from_='+18329003170',
                     to=str(hh.phone)
                 )
            return redirect('home')
        else:
            messages.info(request,'Host email does not exist')
            return redirect('checkin')

    return render(request, 'checkin.html')
    

def checkout(request):
    if request.method=='POST':
        checkout=request.POST['checkout']
        email=request.POST['email']
        datenow=date.today()
        checkout2=str(datenow)+" "+checkout
        if visitor.objects.filter(email=email).exists():
            v=visitor.objects.filter(email=email).order_by('-id')
            if(len(v)==0):
                messages.info(request, 'email is not valid')
                return redirect('checkout')
            v=v[0]
            m=visit.objects.filter(visitor=v, timeout__isnull=True).order_by('-id')
            if(len(m)==0):
                messages.info(request, 'No ongoing meeting')
                return redirect('checkout')
            m=m[0]
            m.timeout=checkout2
            m.save()
            userh=m.host.user
            #userh=User.objects.get(host=temph)
            #userh=temph.user
            subject='Meeting Details with '+userh.first_name+' '+userh.last_name
            message='You, '+v.name+' '+' had a meeting with '+userh.first_name+' '+userh.last_name+'\nCheck-in Time: '+str(m.timein)+'\nCheck-out Time: '+checkout2+"\nLocation: "+m.address+"\nHost Phone No.: "+str(m.host.phone)+"\nHost Email: "+userh.email
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[email,]
            send_mail(subject, message, email_from, recipient_list)
            '''message = client.messages \
                .create(
                     body='You had a meeting with '+userh.first_name+' '+userh.last_name+'\nCheck-in Time: '+str(m.timein)+'\nCheck-out Time: '+checkout2,
                     from_='+18329003170',
                     to=str(v.phone)
                 )'''
            return redirect('home')
        else:
            messages.info(request, 'No meeting is ongoing with this email')
            return redirect('checkout')
    return render(request, 'checkout.html')


def hostview(request):
    if request.user.is_authenticated:
        hid=request.user.host
        allvisits=visit.objects.filter(host=hid)
        context={'allvisits':allvisits}

        return render(request, 'host.html', context)
    else:
        return render(request, 'host.html')