from django.http import HttpResponse
from django.shortcuts import render
def login(request):
    return render(request, 'home.html')

def count(request):
    data = request.GET['fulltextarea']
    word_list = data.split()
    list_lengnth = len(word_list)
    worddictionary = {}

    for word in word_list:
        if word in worddictionary:
            worddictionary[word] += 1
           #increase value by 1
        else:
            worddictionary[word] = 1
       #add to the worddictonary and set value to 1

    return render(request, 'count.html',{'fulltext': data, 'words':list_lengnth, 'worddictionary': worddictionary})
