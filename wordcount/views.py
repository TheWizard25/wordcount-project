from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"hompage.html")

def infopage(request):
    return render(request,"info.html")

def resultpage(request):
    text=request.GET['usertext']
    x=text.split(" ")
    c=len(x)
    mostlist=[]
    countlist=[]
    
    for i in x:
        count=0
        for j in x:
            if(i==j):
                count+=1
        countlist.append(count)
        
    maxcount=max(countlist)
    f=0
    for i in countlist:
        if maxcount==i:
            if x[f] not in mostlist:
                mostlist.append(x[f])
        f+=1
    one=0
    for i in countlist:
        if i!=1 and i!=None:
            one=1
    if one==0:
        most="All words are occuring same number of time."
    elif (len(mostlist)==1):
        most='"'+mostlist[0]+"\" is the most repitive word in the text."
    else:
        most=str(mostlist)+" are the most repitive words in the text."


    return render(request,"resultpage.html",{"text":text,"count":c,"most":most})