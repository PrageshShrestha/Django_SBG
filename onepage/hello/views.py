from tkinter import Button
from django.shortcuts import render
from .models import  Comments,Login
from django.conf import settings
import os 
from playsound import playsound
# from .models import Visitors
# from hitcount.views import HitCountDetailView

English = {
    'home':'Home',
    
    'title':'SBGS',
    'home':'Home',
    'Location':'Location',
    'Befe':'Benefits and Features',
    'Cont':'Contact us',
    'language':'Language',
    'title':'SBGS',
    'Found':'Founded by',
    'found_name':'Panchalal Shrestha',
    'topic_sentence':'Find Your Gents Clothingat Swet Bhairav General Stores . Find Recent Trends In Less ',
    'highlight':'Cause Quality Is King',
    'More_pics':'More Pics',
    'Features':'Features',
    'fe1':'Wide Variety of Cothes . Close in Customer Support',
    'fe2':'hug with big hall Better customer experiance with better price',

    'Feature1':'Boys and Gents Outfits ',
    'f1':'at one place',
    'Feature2':'Shop like Daraz',
    'f2':'But there is a touch lol',
    
    'Feature3': 'find recent trends ',
    'f3':'at our shop ',
    
    'Feature4':'Styling your personality ',
    'f4':'with low cost ',
    'Feature5':'Our Journey Begins when ',
    'f5':'Customers go alive ',
    'contacts':'Contact us at:',
    'number1':9844053689,
    'number2':9801606601,
    'profile':'Our Profile',
    'comments':'Comments',
    'submit':'Submit',
    'like':'like',
    'reply':'reply' ,   
    
}
Nepali = {
    'title':'',
    'home':'',
    'Location':'',
    'Befe':'',
    'Cont':'',
    'language':'',
    'title':'',
    'Found':'',
    'found_name':'',
    'topic sentence':'',
    'highlight':'',
    'More_pics':'',
    'Features':'',
    'Feature1':'',
    'f1':'',
    'Feature2':'',
    'f2':'',
    
    'Feature3': '',
    'f3':'',
    
    'Feature4':'',
    'f4':'',
    'Feature5':'',
    'f5':'',
    'contacts':'Contact us at:',
    'number1':9,
    'number2':9,
    'profile':'',
    'comments':'',
    'submit':'',
    'like':'',
    'reply':'' ,   
    
}

# mainpage
# location
# benefits and features
# contact us 
# language
# ______________
# title = homepage
# Founded by:Panchalal shrestha
# findyour gents clothing at Swet Bhairav General stores. Find recent treends in less price Cause quality is king
# More pics
# Features
# Wide Variety of Cothes . Close in Customer Support hug with big hall Better 
# customer experiance with better price 
# Boys and Gents Outfits 
# at one place
# Get oxiticin with Us 
# find recent trends at our shop 
# Styling your personality 
# with low cost 
# Our Journey Begins when 
# Customers go alive 
# ____________________________
# Contacts 
# 9845022298
# 9801606601
# our Profile 
# Panchalal Shrestha 
# ___________________________
# Comments 
# name:
# submit like reply






def hello2(request):
    hello = Login.objects.all()
    if request.method == 'POST':
        agent = Login()
        agent.login = request.POST.get('login_email')
        agent.password = request.POST.get('login_password')
        if request.POST.get('remember'):
            agent.keep_logged = True
        else:
            agent.keep_logged = False  
              
        agent.save()
    # path = settings.MEDIA_ROOT
    # img_list = os.listdir(path + 'static/media/pictures')
    # context = {"images": img_list}
    # return render (request, '(path to django template)', context)    
    return render(request , 'login1.html')    
def hello(request):
    
    hello = Comments.objects.all()
    #if Button:
       # playsound('static/beep.mp3')
   
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    
    # device_type = ""
    # browser_type = ""
    # browser_version = ""
    # os_type = ""
    # os_version = ""
    # if request.user_agent.is_mobile:
    #     device_type = "Mobile"
    # if request.user_agent.is_tablet:
    #     device_type = "Tablet"
    # if request.user_agent.is_pc:
    #     device_type = "PC"
    
    # browser_type = request.user_agent.browser.family
    # browser_version = request.user_agent.browser.version_string
    # os_type = request.user_agent.os.family
    # os_version = request.user_agent.os.version_string
    # Visitors.Browser_type = browser_type
    # Visitors.Ip = ip
    # Visitors.Browser_version = browser_version
    # Visitors.OS_type = os_type
    # Visitors.os_version = os_version
           
    if request.method =='POST':
        agent = Comments()
        agent.comments = request.POST.get('opinion')
        agent.save()
    if 'Language' in request.POST:
        language = Nepali
    else:
        language = English     
    return render(request , 'homepage.html',{'English':language ,'comment':hello , 'range' :range(14)})    
print(hello)  
  
       
# Create your views here.
 