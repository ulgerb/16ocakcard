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
    image = models.FileField(("Resim"), upload_to="", max_length=100)
    date_now = models.DateTimeField(("Tarih - Saat"), auto_now_add=True)
    author = models.CharField(("Yazar"), max_length=50)

    def __str__(self):
        return self.title
