from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    cards = Card.objects.all()
    category = Category.objects.all()
    context={
        "cards":cards,
        "category": category,
    }
    return render(request,'index.html',context)

def Detail(request,did):
    card = Card.objects.get(id=did)
    context={
        "card":card,
    }
    return render(request,'detail.html',context)

# CATEGORY
def allCard(request,cid):
    
    if cid == "all":
        cards = Card.objects.all()
    else:
        cards = Card.objects.filter(category__title=cid) 
    
    category = Category.objects.all()
    
    context = {
        "cards": cards,
        "category":category,
        "cid": cid,
    }
    return render(request,'all_card.html',context)