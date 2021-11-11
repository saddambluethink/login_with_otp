from django.db.models.base import ModelBase
from django.http import response
from django.http.request import HttpRequest
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from .models import Profile
# for send otp
import os
# pip install twilio
from twilio.rest import Client
# Create your views here.
import random
import requests


def login(request):
    if request.method=='POST':
        mob=request.POST['mobile']
        
        print("=========",mob)
        otp=str(random.randint(1000,9999))
        print("otp=======",otp)
        data=Profile.objects.create(mobile=mob,otp=otp)
        #data.save()
        account_sid = 'ACe696e7ccff7d7f60d890cdc26c4f996c'
        auth_token = 'f316918f10a2e21e42cc3b84b2681ecb'
        client = Client(account_sid, auth_token)

        message = client.messages.create(body="this is verify otp"+str(otp),
                            from_='+18066055118',
                            to='+918814024487')
        print(message.sid)
        print("otp send=============================================================")
                        
        mobile=mob
        return render(request,'otp.html',{'mob':mobile})
        
    return render(request,'login.html')





def otp(request):
    if request.method=='POST':
        otpp=request.POST['otp']
        mob=request.POST['mobile']
        print("====mob",mob)
        print("====",otp)
        p=Profile.objects.filter(mobile=mob,otp=otpp)
        if p :
             return HttpResponse("you are logged here")
        
        return HttpResponse("otp invalid")
    #return render(request,'otp.html')
    







         # get api data

def home(request):
    response=requests.get('https://reqres.in/api/users').json()
    response["data"]

    # by id
    res=requests.get('https://reqres.in/api/users/1').json()
    res["data"]

    #get resourse
    
    ress=requests.get('https://reqres.in/api/unknown').json()
    ress["data"]
    
    #get by id
    # re=requests.get('https://reqres.in/api/unknown').json()
    # re["data"]
    return render(request,'home.html',{'response':response["data"],'data':res["data"],'dataa':ress["data"]})
        


