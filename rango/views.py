from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, cupcake!"}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'my_name': "Jorge"}
    return render(request, 'rango/about.html', context_dict)


def cat(request):
    context_dict = {'boldmessage': "I Sleep!",
                    'cat_name':"Roro",
                    'favorite_food':"Tuna"    
                }
    return render(request, 'rango/cat.html', context_dict)