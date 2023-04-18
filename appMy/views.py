from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from django.db.models import Q, Count
from django.contrib.auth import authenticate, login , logout # giriş ve çıkış için
from django.contrib.auth.models import User # kullanıcı modeli kayıt etmek için views'e import edildi

# Create your views here.

def index(request):
    cards = Card.objects.filter(active=True)
    category = Category.objects.all()
    brands = Card.objects.values('brand').annotate(Count('brand'))
    print(brands)
    context={
        "cards":cards,
        "category": category,
        "brands": brands,
    }
    return render(request,'index.html',context)

def Detail(request,did):
    card = Card.objects.get(id=did)
    comments = Comment.objects.filter(card=card)
    # yorumları çek, 
    
    if request.method == "POST":
        name = request.POST.get("name")
        text = request.POST.get("text")

        comment = Comment(name=name, text=text, card = card)
        comment.save()
        return redirect('/detail/'+ did +'/')  # Yönlendirme
    
    context={
        "card":card,
        "comments": comments,
    }
    return render(request,'detail.html',context)



# CATEGORY
def allCard(request,cid=None):
    
    if cid == None:
        cards = Card.objects.filter(active=True)
    elif cid == "all":
        cards = Card.objects.filter(active=True)
    else:
        cards = Card.objects.filter(Q(category__title=cid) | Q(brand=cid) , active=True) 
    
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
        return redirect("Contact")

    context={}
    return render(request,'contact.html',context)

# CARD CREATE
def cardCreate(request):
    categorys = Category.objects.all()
    
    
    if request.method == "POST":
        category = Category.objects.get(id = request.POST.get("category"))
        title = request.POST.get("title")  
        text = request.POST.get("text")
        author = request.POST.get("author")
        brand = request.POST.get("brand")
        image = request.FILES.get("image") # html'de enctype="multipart/form-data"
        print("ACTİVE:==========",request.POST.get("active"))

        active = request.POST.get("active")
        if active is None:
            active = False
        
        card = Card(title=title, text=text, author=author, brand=brand, category=category, active=active)
        if image is not None:
            card.image = image
        card.save()
        return redirect("/")
        
    context = {
        "categorys":categorys,
    }
    return render(request, "card/card-create.html", context)


# USER ======================================

def loginUser(request): # GET

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # DATA'da bu kullanıcı varmı, varsa bilgileri kontrol et, eğer doğruysa sisteme giriş yapsın
        user = authenticate(username=username, password=password) # DATA'da kullanıcı varsa bilgileri kontrol ediyor, 
        # eğerki kullanıcı var ve bilgiler doğruysa bize bilgileri geri döndürüyor 
        #  eğer kullanıcı yok veya bilgileri yanlışsa None değeri döndürür
        
        if user is not None: # None değilse 
            login(request, user)
            return redirect("index")
        else:
            hata = "Kullanıcı adı veya şifre yanlış!"
            context = {"hata": hata}
            return render(request, 'user/login.html', context)
            
    
    context = {}
    return render(request, 'user/login.html', context)


def registerUser(request):
    
   
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        # şifreler eşit , email ve username DATA'da olmaması gerekir, sözleşmeyi doğruladımı
        
        if password1 == password2:
            if not User.objects.filter(username=username).exists(): # exists içi doluysa true döndürür
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(email=email, username=username, password=password2, first_name = name)
                    user.save()
                    return redirect("loginUser")
                else:
                    context = { "hata":"Bu email zaten kullanılıyor!" }
                    return render(request, "user/register.html", context)
            else:
                return render(request, "user/register.html", {"hata": "Bu kullanıcı zaten kullanılıyor!"})
        else:
            return render(request, "user/register.html", {"hata": "şifreler aynı değil!"})
                
    
    context = {}
    return render(request, "user/register.html", context)


def logoutUser(request):
    logout(request)
    return redirect("loginUser")