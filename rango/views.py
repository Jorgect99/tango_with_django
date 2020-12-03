from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm
from datetime import datetime


def index(request):
    request.session.set_test_cookie()

    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
   
    context_dict = {'categories': category_list, 'pages': pages_list}

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'rango/index.html', context_dict)

    return response

def get_server_side_cookie(request, cookie, default_value=None):
    val = request.session.get(cookie)
    if not val:
        val = default_value
    return val

#cookie 
def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))

    last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],'%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1

        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_vist'] = last_visit_cookie
        
    request.session['visits'] = visits



def about(request):
    if request.session.test_cookie_worked():
        print("TEST COOKIED WORKED!!")
        request.session.delete_test_cookie()


    context_dict = {'my_name': "Jorge"}

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'rango/about.html', context_dict)
    
    return response


def cat(request):
    context_dict = {'boldmessage': "I Sleep!",
                    'cat_name':"Roro",
                    'favorite_food':"Tuna"    
                }
    return render(request, 'rango/cat.html', context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        

        context_dict['pages'] = pages

        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    form =  CategoryForm()
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            cat = form.save(commit=True)
            print(cat,cat.slug)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'rango/add_category.html',{'form': form})


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0 
                page.save()
        else:
            print(form.errors)

    context_dict = {'form':form, 'category':category}

    return render(request, 'rango/add_page.html', context_dict)