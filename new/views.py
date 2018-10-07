from django.shortcuts import render,get_object_or_404
from .models import Habar,TDSGZ,Gosmaca,Slideshow,Renkler,Menu,Myhmanlar,Gif_lar,Habar_Surat,Fayl,Sorag_Jogap,Albom,Surat,Video
from django.http import HttpResponse
from datetime import datetime,timedelta
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def not_found(request):
    render(request,'not_found.html')

def fun(pk,client):
    global vs,now,today,yesterday,asd,dil,Gosmacalar,active,Slide,Renk,Menular,asd,Giflar,Habarlar,hab_surat,fayls,moh
    if 'dil' not in client.session: client.session['dil']='tm'
    if(client.POST):
        client.session['dil']=client.POST['dil']
    dil=client.session['dil']

    vs=1
    print(client.session['dil'])
    client_ip = client.META['REMOTE_ADDR']
    for Myhman in reversed(Myhmanlar.objects.all()):
        if(Myhman.Ip_adresleri==client_ip and Myhman.updated_at.day==datetime.today().day):
            vs=0
            Myhman.updated_at=datetime.today()
            Myhman.save()
            break
    if(vs):
        Myhmanlar.objects.create(Ip_adresleri=client_ip)
    asd=len(Myhmanlar.objects.all())

    now =len(Myhmanlar.objects.filter(updated_at__minute=datetime.today().minute))
    today =len(Myhmanlar.objects.filter(updated_at__day=datetime.today().day))
    yesterday = len(Myhmanlar.objects.filter(updated_at__day=(datetime.today()-timedelta(days=1)).day))

    Gosmacalar=Gosmaca.objects.all()
    Renk=Renkler.objects.all()
    Menular = Menu.objects.all()

    if(pk!='mohum-habar' and pk!='sorag-jogap'):
        if(dil=='en'):
            active=Menu.objects.get(Slug=pk).Ady_en
        elif(dil=='ru'):
            active = Menu.objects.get(Slug=pk).Ady_ru
        else:
            active=Menu.objects.get(Slug=pk).Ady_tm

def index(request):
    fun('mohum-habar',request)
    Slide = Slideshow.objects.all()
    if (dil == 'en'):
        active = Menular[0].Ady_en
    elif (dil == 'ru'):
        active = Menular[0].Ady_ru
    else:
        active = Menular[0].Ady_tm
    k=[]
    for i in range(1,10):
        k.append(Habar.objects.order_by('-Wagty').filter(Menu=i))
    moh=Habar.objects.filter(Mohum=True)
    Giflar = Gif_lar.objects.all()
    aba={'Yokarsy':TDSGZ.objects.get(id=1),'Gosmaca':Gosmacalar,'active':active,'Slide':Slide,'Shuwagt':now,'Sugun':today,'Duyn':yesterday,'Jemi':asd,'dil':dil,'Menu':Menular,'Gif':Giflar,
         'moh_hb':moh,'k':k}
    return render(request,'index.html',aba)

def additional(request,pk):
    # request.session['asd']='as'
    get_object_or_404(Menu,Slug=pk)
    fun(pk,request)
    if(pk=='harby-hukuk'):
        fayls = Fayl.objects.all()
        aba = {'Yokarsy': TDSGZ.objects.get(id=1), 'Gosmaca': Gosmacalar, 'active': active,'Menu': Menular, 'Shuwagt': now, 'Sugun': today, 'Duyn': yesterday, 'Jemi': asd, 'dil': dil,
               'fayl': fayls}
        return render(request, 'harby-hukuk.html', aba)
    elif(pk=='multimediya'):
        Giflar = Gif_lar.objects.all()
        Albomlar=Albom.objects.all()
        aba = {'Yokarsy': TDSGZ.objects.get(id=1), 'Gosmaca': Gosmacalar, 'active': active,'Menu': Menular, 'Shuwagt': now, 'Sugun': today, 'Duyn': yesterday, 'Jemi': asd, 'dil': dil,
               'Habar': Albomlar,'Gif':Giflar}
        return render(request, 'multimediya.html', aba)
    elif(pk=='sorag-jogap'):
        soraglar = Sorag_Jogap.objects.all()
        aba = {'Yokarsy': TDSGZ.objects.get(id=1), 'Gosmaca': Gosmacalar, 'Menu': Menular, 'Shuwagt': now, 'Sugun': today, 'Duyn': yesterday, 'Jemi': asd, 'dil': dil,
               'surat': soraglar}
        return render(request,'sorag-jogap.html',aba)
    else:
        if (pk == 'mohum-habar'):
            Habarla = Habar.objects.filter(Mohum=True)
        else:
            Habarla = Habar.objects.filter(Menu__Slug=pk)
        page = request.GET.get('page', 1)
        paginator = Paginator(Habarla, 10)
        try:
            Habarlar = paginator.page(page)
        except PageNotAnInteger:
            Habarlar = paginator.page(1)
        except EmptyPage:
            Habarlar = paginator.page(paginator.num_pages)
        aba = {'Yokarsy': TDSGZ.objects.get(id=1), 'Gosmaca': Gosmacalar, 'active': active,'Menu': Menular, 'Shuwagt': now, 'Sugun': today, 'Duyn': yesterday, 'Jemi': asd, 'dil': dil,
               'Habar': Habarlar}

        return render(request,'additional.html',aba)
def habar(request,pk):#cozuldi
    fun('mohum-habar',request)
    hab_surat = Habar_Surat.objects.filter(Habar_ady=pk)
    # Habarlar = Habar.objects.get(id=pk)
    Habarlar = get_object_or_404(Habar,id=pk)
    Habarlar.Okalan = Habarlar.Okalan + 1
    Habarlar.save()
    aba = {'Yokarsy': TDSGZ.objects.get(id=1), 'Gosmaca': Gosmacalar, 'Menu': Menular, 'Shuwagt': now,'Sugun': today, 'Duyn': yesterday, 'Jemi': asd, 'dil': dil,
           'Habar': Habarlar,'surat':hab_surat}
    return render(request,'post-only.html',aba)


def albom(request,pk):#cozuldi
    fun('mohum-habar',request)
    get_object_or_404(Albom,id=pk)
    sur = Surat.objects.filter(Ady__id=pk)
    Giflar = Gif_lar.objects.all()
    aba={'Yokarsy': TDSGZ.objects.get(id=1), 'Gosmaca': Gosmacalar, 'Menu': Menular, 'Shuwagt': now,'Sugun': today, 'Duyn': yesterday, 'Jemi': asd, 'dil': dil,
         'sur': sur,'Gif':Giflar}
    return render(request,'albom.html',aba)
def videos(request):
    fun('mohum-habar',request)
    vid=Video.objects.all()
    Giflar = Gif_lar.objects.all()
    aba={'Yokarsy': TDSGZ.objects.get(id=1), 'Gosmaca': Gosmacalar, 'Menu': Menular, 'Shuwagt': now,'Sugun': today, 'Duyn': yesterday, 'Jemi': asd, 'dil': dil,
         'vid': vid,'Gif':Giflar}
    return render(request,'video.html',aba)

def video(request,pk):
    fun('mohum-habar',request)
    Giflar = Gif_lar.objects.all()
    # vid=Video.objects.get(id=pk)
    vid=get_object_or_404(Video,id=pk)
    print(vid)
    aba={'Yokarsy': TDSGZ.objects.get(id=1), 'Gosmaca': Gosmacalar, 'Menu': Menular, 'Shuwagt': now,'Sugun': today, 'Duyn': yesterday, 'Jemi': asd, 'dil': dil,
         'vid': vid,'Gif':Giflar}
    return render(request,'watch.html',aba)
