from django.shortcuts import render


def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html' , {'content':['If you would like to contact me, please email me','bhargav.kulkarni1@gmail.com']})

def about(request):
    return render(request, 'personal/basic2.html' , {'content':['Hello, I am Bhargav Kulkarni. I am a highschooler currently studying in NPS HSR.' ,
                                                               'I enjoy programming(I built this entire site by myself) and I like watching anime and movies.',
                                                               'Welcome to my inner thoughts.']})
