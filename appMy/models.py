from django.db import models

class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    content = models.CharField(("Deneme Yeri"), max_length=50, null=True)
    
    def __str__(self):
        return self.title


# foreignkey modeli başka modeli referans alır bilgilerini içinde tutar, seçme inputu verir
class Card(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("İçerik Yazısı"), max_length=1000)
    image = models.FileField(("Resim"), upload_to="", max_length=100, default='logo.jpg')
    date_now = models.DateTimeField(("Tarih - Saat"), auto_now_add=True, null=True)
    author = models.CharField(("Yazar"), max_length=50)
    brand = models.CharField(("Marka"), max_length=50, null=True)
    active = models.BooleanField(("Göster"), default=False)


    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"

class ContactModel(models.Model):
    title = models.CharField(("Konu"), max_length=50)
    text = models.TextField(("Mesaj"), max_length=2000)
    email = models.EmailField(("Email"), max_length=254)
    name = models.CharField(("İsim"), max_length=50)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    card = models.ForeignKey(Card, verbose_name=("Ürün"), on_delete=models.CASCADE)
    name = models.CharField(("İsim"), max_length=50)
    text = models.TextField(("Yorum"), max_length=2000)
    date_now = models.DateTimeField(("Tarih- Saat"), auto_now_add=True)
    
    def __str__(self):
        return self.card.title

    class Meta:
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"
