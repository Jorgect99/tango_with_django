import os 
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    Category.objects.all().delete()
    Page.objects.all().delete()
    
    python_pages = [
        {"title":"Oficial Python Tutorial","url":"http://dics.python.org/2/tutorial/"},
        {"title":"How to think like a computer scientist","url":"http://www.greenteapress.com/thinkpython"},
        {"title":"Learn Python in 10 minutes","url":"http://www.korokithakis.net/tutorials/python"},
    ]

    django_pages = [
        {"title":"Official Django Tutorial","url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01"},
        {"title":"Django Rocks","url":"http://djangorocks.com/"},
        {"title":"How to Tango with Django","url":"http://www.tangowithdjango.com"},
    ]

    other_pages = [
        {"title":"Bottle","url":"http://bottlepy.org/docs/dev/"},
        {"title":"Flask","url":"http://flask.pocoo.org"},
    ]

    cats = {
        "Python":{"pages":python_pages, "views":128, "likes":64},
        "Django":{"pages":django_pages, "views":64, "likes":32},
        "Other Frameworks":{"pages":other_pages, "views":32, "likes":16},
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c,p["title"], p["url"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category = c):
            print("- {0} - {1}".format(str(c), str(p)))
 

def add_page(cat, title, url):
    p = Page.objects.get_or_create(category = cat, title = title)[0]
    p.url = url 
    p.views = random.randint(0, 100)
    p.save()

    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.lies = likes
    c.save()
    return c

if __name__=='__main__':
    print("Staring Rango population script")
    populate()