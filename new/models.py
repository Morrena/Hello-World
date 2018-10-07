from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
import os
# Create your models here.
class Menu(models.Model):
    Ady_tm = models.CharField(max_length=70)
    Ady_ru = models.CharField(max_length=70,default='')
    Ady_en = models.CharField(max_length=70,default='')
    Slug = models.CharField(max_length=70,default='')
    Sahypa_suraty = models.ImageField(blank=True,upload_to='Sahypa_Suraty')
    Habar = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Ady_tm

class Habar(models.Model):
    Menu = models.ForeignKey(Menu,on_delete=models.CASCADE,limit_choices_to={'Habar':True})
    Ady_tm = models.CharField(max_length=70)
    Ady_ru = models.CharField(max_length=70,default='')
    Ady_en = models.CharField(max_length=70,default='')
    Wagty = models.DateField(null=True)
    Okalan = models.IntegerField(default=0)
    Esasy_Surat = models.ImageField(blank=True,upload_to='Habar')
    Makala_tm = models.TextField(null=True)
    Makala_ru = models.TextField(blank=True)
    Makala_en = models.TextField(blank=True)
    Mohum = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Fayl(models.Model):
    Ady_tm = models.CharField(max_length=70,default='')
    Ady_ru = models.CharField(max_length=70,default='')
    Ady_en = models.CharField(max_length=70,default='')
    Mazmun_tm = models.TextField(blank=True)
    Mazmun_ru = models.TextField(blank=True)
    Mazmun_en = models.TextField(blank=True)
    Pdf = models.FileField(upload_to='Kitaplar')
    Ikonka = models.ImageField(upload_to='Kitaplar',blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Ady_tm

class Slideshow(models.Model):
    Esasy_Slide=models.CharField(default='Esasy-Slide',max_length=70)
    Slide1_1_tm = models.CharField(blank=True,max_length=100)
    Slide1_1_ru = models.CharField(blank=True,max_length=100)
    Slide1_1_en = models.CharField(blank=True,max_length=100)
    Slide1_1_url = models.CharField(blank=True,max_length=100)
    Slide1_1 = models.ImageField(upload_to='SlideShow')
    Slide1_2_tm = models.CharField(blank=True,max_length=100)
    Slide1_2_ru = models.CharField(blank=True,max_length=100)
    Slide1_2_en = models.CharField(blank=True,max_length=100)
    Slide1_2_url = models.CharField(blank=True,max_length=100)
    Slide1_2 = models.ImageField(upload_to='SlideShow')
    Slide1_3_tm = models.CharField(blank=True,max_length=100)
    Slide1_3_ru = models.CharField(blank=True,max_length=100)
    Slide1_3_en = models.CharField(blank=True,max_length=100)
    Slide1_3_url = models.CharField(blank=True,max_length=100)
    Slide1_3 = models.ImageField(upload_to='SlideShow')
    Slide2_1_tm = models.CharField(blank=True,max_length=100)
    Slide2_1_ru = models.CharField(blank=True,max_length=100)
    Slide2_1_en = models.CharField(blank=True,max_length=100)
    Slide2_1_url = models.CharField(blank=True,max_length=100)
    Slide2_1 = models.ImageField(upload_to='SlideShow')
    Slide2_2_tm = models.CharField(blank=True,max_length=100)
    Slide2_2_ru = models.CharField(blank=True,max_length=100)
    Slide2_2_en = models.CharField(blank=True,max_length=100)
    Slide2_2_url = models.CharField(blank=True,max_length=100)
    Slide2_2 = models.ImageField(upload_to='SlideShow')
    Slide2_3_tm = models.CharField(blank=True,max_length=100)
    Slide2_3_ru = models.CharField(blank=True,max_length=100)
    Slide2_3_en = models.CharField(blank=True,max_length=100)
    Slide2_3_url = models.CharField(blank=True,max_length=100)
    Slide2_3 = models.ImageField(upload_to='SlideShow')
    Slide3_1_tm = models.CharField(blank=True,max_length=100)
    Slide3_1_ru = models.CharField(blank=True,max_length=100)
    Slide3_1_en = models.CharField(blank=True,max_length=100)
    Slide3_1_url = models.CharField(blank=True,max_length=100)
    Slide3_1 = models.ImageField(upload_to='SlideShow')
    Slide3_2_tm = models.CharField(blank=True,max_length=100)
    Slide3_2_ru = models.CharField(blank=True,max_length=100)
    Slide3_2_en = models.CharField(blank=True,max_length=100)
    Slide3_2_url = models.CharField(blank=True,max_length=100)
    Slide3_2 = models.ImageField(upload_to='SlideShow')
    Slide3_3_tm = models.CharField(blank=True,max_length=100)
    Slide3_3_ru = models.CharField(blank=True,max_length=100)
    Slide3_3_en = models.CharField(blank=True,max_length=100)
    Slide3_3_url = models.CharField(blank=True,max_length=100)
    Slide3_3 = models.ImageField(upload_to='SlideShow')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Esasy_Slide

class Gosmaca_Ady(models.Model):
    Ady = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Ady

class Gosmaca(models.Model):
    Sayla = models.ForeignKey(Gosmaca_Ady,on_delete=models.CASCADE)
    Surat_tm = models.ImageField(upload_to='Gosmaca',blank=True)
    Surat_en = models.ImageField(upload_to='Gosmaca',blank=True)
    Surat_ru = models.ImageField(upload_to='Gosmaca',blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Sayla.Ady

class Renk_Ady(models.Model):
    Ady = models.CharField(max_length=70);
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Ady

class Renkler(models.Model):
    Sayla = models.ForeignKey(Renk_Ady,on_delete=models.CASCADE)
    Renk_kody = models.CharField(max_length=70,default=None)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Sayla.Ady

class TDSGZ(models.Model):
    Tm = models.CharField(max_length=170,default='')
    Ru = models.CharField(max_length=170,default='')
    En = models.CharField(max_length=170,default='')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Myhmanlar(models.Model):
    Ip_adresleri = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Habar_Surat(models.Model):
    Habar_ady = models.ForeignKey(Habar,models.CASCADE)
    Suraty = models.ImageField(upload_to='Habar_Surat',blank=True)

class Gif_lar(models.Model):
    Ady = models.CharField(default='',max_length=70)
    Bas_Arkafon = models.ImageField(upload_to='Gif_lar')
    Bas_Usti = models.ImageField(upload_to='Gif_lar')
    Bas_Gif = models.ImageField(upload_to='Gif_lar')
    Media_Surat = models.ImageField(upload_to='Gif_lar')
    Media_Video = models.ImageField(upload_to='Gif_lar')
    def __str__(self):
        return self.Ady

class Sorag_Jogap(models.Model):
    Sorag_tm= models.CharField(max_length=70)
    Jogap_tm=models.TextField()
    Sorag_ru= models.CharField(max_length=70)
    Jogap_ru=models.TextField()
    Sorag_en= models.CharField(max_length=70)
    Jogap_en=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Video(models.Model):
    Ady_tm = models.CharField(max_length=70,default='')
    Ady_en = models.CharField(max_length=70,default='')
    Ady_ru = models.CharField(max_length=70,default='')
    Vidyo = models.FileField(upload_to='Video')
    Vidyo_Surat = models.ImageField(upload_to='Video',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Ady_tm

class Albom(models.Model):
    Ady_tm = models.CharField(max_length=70,default='')
    Ady_en = models.CharField(max_length=70,default='')
    Ady_ru = models.CharField(max_length=70,default='')
    Esasy_Surat = models.ImageField(upload_to='Albom',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Ady_tm

class Surat(models.Model):
    Ady = models.ForeignKey(Albom,on_delete=models.CASCADE)
    Surat = models.ImageField(blank=True,upload_to='Albom')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

@receiver(models.signals.pre_save, sender=Gif_lar)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).file
    except sender.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)