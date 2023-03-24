from django.shortcuts import render
from .models import *
from django.db.models import Q

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
        cards = Card.objects.filter(Q(category__title=cid) | Q(brand=cid)) 
    
    category = Category.objects.all()
    
    context = {
        "cards": cards,
        "category":category,
        "cid": cid,
    }
    return render(request,'all_card.html',context)


def Contact(request):
    # normalde sayfa ve fonksiyon GET ile çalışır 
    if request.method == "POST":
        
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        mess = request.POST.get("message")

        contact = ContactModel(title=subject, text=mess, email=email, name=name)
        contact.save()
    

    context={}
    return render(request,'contact.html',context)