from gzip import READ
import re
from django.shortcuts import render
from django.http import HttpResponse


from .models import MySkill







def home(request):

    item = MySkill.objects.all()

    # return HttpResponse("This is home page!")
    title = 'Welcome to Quietsos'
    desc =  'What is IoT? The Internet of Things (IoT) describes the network of physical objects—“things”—that are embedded with sensors, software, and other technologies for the purpose of connecting and exchanging data with other devices and systems over the internet.'
    
    context = {
        'title':title,
        'description':desc,
        'data': item,

    }
      
    return render(request,'index.html',context)



def contact(request):
    # return HttpResponse("This is contact page!")

    name = request.GET.get('name')
    email = request.GET.get('email')
    query = request.GET.get('comments')

    # print(name)
    # print(email)
    # print(query)

    print(f" name:{name} \n Email: {email} \n Query: {query} \n")

    
    return render(request,'demo/contact.html')

def about(request):
    # return HttpResponse("This is about page")
    title = "About Me"
    desc = """Internet of Things (IoT) is the network of connected objects that c
    ontains embedded technology within them to communicate and interact with the 
    physical environment. The term Internet of Things collectively refers to all 
    these connected things and the technologies that enable them to communicate among 
    themselves and with the external environment. They are typically used for the automation 
    of menial tasks and monitoring purposes. With a vast diversity of technology, 
    the Internet of Things finds its application in various sectors ranging from general 
    consumer uses to large scale industrial use cases. Nowadays, IoT is widely accepted in workplaces, 
    which brings about considerable enhancements in business processes and technologies.
    However, an efficient UEM solution capable of managing IoT along with
    other common device platforms is a vital requirement for such organizations
    that adopt IoT in the Enterprise, which is commonly known as Enterprise of Things or EoT."""
   
    context = {
        'title': title,
        'aboutDesc' : desc,
    }
   
    return render(request,'demo/about.html', context)


    


