from django.db import models


class Header(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField()
    phone = models.IntegerField()
    telegram_link = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    

class Navbar(models.Model):
    name = models.CharField(max_length=255)
    imges = models.ImageField()


    def __str__(self) -> str:
       return self.imges
    



class Tarif(models.Model):
    ekanom = models.CharField(max_length=255)
    komfort = models.CharField(max_length=255)
    lyuks = models.CharField(max_length=255)
    


class Travel(models.Model):
    Tarif = models.ForeignKey(Tarif, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    Aviakompaniya = models.CharField(max_length=255)
    Duration = models.IntegerField()
    food = models.BooleanField()
    visa = models.CharField(max_length=255)
    help = models.IntegerField()
    Jilet = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    



    

