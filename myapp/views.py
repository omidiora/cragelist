import requests
from django.shortcuts import render
from requests.compat import quote_plus
from bs4 import BeautifulSoup
from .models import Search
from . import models

# Create your views here.
BASE_CRAIGSLIST_URL="https://johannesburg.craigslist.org/d/education-teaching/search/edu"
def home(request):
    return render(request,'base.html')

def new_search(request):
    search=request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url=BASE_CRAIGSLIST_URL.format(quote_plus(search)) 
    response=requests.get(final_url)
    data=response.text
    print(data)

    stuff_for_frontend={
        'search':search

    }
    return render(request,'myapp/new_search.html',stuff_for_frontend)
