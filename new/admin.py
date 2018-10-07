from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Habar,Menu,Fayl,Surat,Albom,Slideshow,Video,Gosmaca_Ady,Gosmaca,Renkler,Renk_Ady,TDSGZ,Myhmanlar,\
    Habar_Surat,Gif_lar,Sorag_Jogap

AdminSite.site_header = 'SERHET ADMIN'
AdminSite.site_title = 'REDAKTOR'
AdminSite.site_url = '/serhetabat-dovletabat'
AdminSite.index_title = 'Saýt administrasiýa'
# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    search_fields = ['Ady_tm']
    pass

admin.site.register(Menu,MenuAdmin)

class Habar_Surat_Inline(admin.StackedInline):
    model = Habar_Surat
    extra = 3

class HabarAdmin(admin.ModelAdmin):
    list_filter = ['Menu']
    list_per_page = 10
    list_display = ('Ady_tm','Menu','Wagty','Okalan')
    search_fields = ['Ady_tm']
    fields = ('Menu',('Ady_tm','Wagty'),('Ady_ru','Esasy_Surat'),('Ady_en','Mohum'),'Makala_tm','Makala_en','Makala_ru')
    inlines = [Habar_Surat_Inline]

admin.site.register(Habar,HabarAdmin)

class FaylAdmin(admin.ModelAdmin):
    fields = ('Ady_tm',('Ady_ru','Ikonka'),('Ady_en','Pdf'),'Mazmun_tm','Mazmun_ru','Mazmun_en')
    pass

admin.site.register(Fayl,FaylAdmin)

class SlideshowAdmin(admin.ModelAdmin):
    readonly_fields = ['Esasy_Slide']
    pass

admin.site.register(Slideshow,SlideshowAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ['Ady_tm']
    pass

admin.site.register(Video,VideoAdmin)

class Albom_Surat_Inline(admin.StackedInline):
    model = Surat
    extra = 3

class AlbomAdmin(admin.ModelAdmin):
    inlines = [Albom_Surat_Inline]

admin.site.register(Albom,AlbomAdmin)

class MyhmanAdmin(admin.ModelAdmin):
    # date_hierarchy = 'created_at'
    list_display = ('Ip_adresleri','updated_at')
    list_filter = ['updated_at']
admin.site.register(Myhmanlar,MyhmanAdmin)
class SoragAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sorag_Jogap,SoragAdmin)
# admin.site.register(Gosmaca_Ady)
admin.site.register(Gosmaca)
admin.site.register(Renkler)
admin.site.register(TDSGZ)
class GifAdmin(admin.ModelAdmin):
    exclude = ['Ady']
admin.site.register(Gif_lar,GifAdmin)
#admin.site.register(Renk_Ady)
