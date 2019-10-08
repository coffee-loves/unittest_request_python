from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import  Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.
def index(request):
#    return HttpResponse("Hello world!")
   return render(request,"index.html")

def login_action(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password = password)
        if user is not None:
            auth.login(request,user)
        if username == 'admin' and password == 'admin123':
           # return  HttpResponse("LOGIN SUCCESS")
            response =  HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user',username,3600)
            request.session['user'] = username #将session信息记录到浏览器
            return  response
        else:
            return  render(request,'index.html',{'error':'username or password error！'})

@login_required
def event_manage(request):
    #username = request.COOKIES.get('user','')
    event_list = Event.objects.all()
    username = request.session.get('user','')  #读取浏览器session
    return render(request,"event_manage.html",{"user":username,"events":event_list})


# 发布会名称搜索
@login_required
def search_name(request):
    username = request.session.get('username', '')
    search_name = request.GET.get("name", "")
    search_name_bytes = search_name.encode(encoding="utf-8")
    event_list = Event.objects.filter(name__contains=search_name_bytes)
    return render(request, "event_manage.html", {"user": username, "events": event_list})


# 嘉宾管理
@login_required
def guest_manage(request):
    guest_list = Guest.objects.all()
    username = request.session.get('username', '')

    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型, 取第一页.
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username, "guests": contacts})

# 嘉宾手机号搜索
@login_required
def search_phone(request):
    username = request.session.get('username', '')
    search_phone = request.GET.get("phone", "")
    search_phone_bytes = search_phone.encode(encoding="utf-8")
    guest_list = Event.objects.filter(phone__contains=search_phone_bytes)

    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username, "guests": contacts,"phone":search_phone})