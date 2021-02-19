from django.shortcuts import render
from django.http import HttpResponse
import requests
import lxml
from bs4 import BeautifulSoup as bs

# Create your views here.

def Index(request):
    return render(request, 'google.html')

def Search(request):
    if request.method == 'POST':
        search = request.POST['search']
        url = 'https://www.ask.com/web?q=' + search
        res = requests.get(url)
        s = bs(res.text, 'lxml')
        result_ls = s.find_all('div', {'class': 'PartialSearchResults-item'})
        find_ls = []

        for r in result_ls:
            r_t = r.find(class_='PartialSearchResults-item-title').text
            r_u = r.find('a').get('href')
            r_d = r.find(class_='PartialSearchResults-item-details').text

            find_ls.append((r_t, r_u, r_d))

        context = {
            'find_ls': find_ls
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')


