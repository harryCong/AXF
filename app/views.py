import hashlib
import uuid

from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from AXF import settings
from app.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtypes, Goods, User, Cart
import os

# 首页
def home(request):

    wheels = Wheel.objects.all()

    navs = Nav.objects.all()

    mustbuys = Mustbuy.objects.all()

    shoplist = Shop.objects.all()
    shophead = shoplist[0]
    shoptabs = shoplist[1:3]
    shopclasss = shoplist[3:7]
    shopcommends = shoplist[7:11]

    mainshows = Mainshow.objects.all()

    data = {
        'title': '首页',
        'wheels': wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shophead':shophead,
        'shoptabs':shoptabs,
        'shopclasss':shopclasss,
        'shopcommends':shopcommends,
        'mainshows':mainshows
    }
    return render(request,'home.html',context=data)

# 闪购超市
def market(request,categoryid,childid,sortid):

    foodtypes = Foodtypes.objects.all()
    # goodlist = Goods.objects.all()

    typeindex = int(request.COOKIES.get('index',0))
    categoryid = foodtypes[typeindex].typeid
    # goodlist = Goods.objects.filter(categoryid=foodtypes[typeindex].typeid)

    # 子类
    childtypename = foodtypes.get(typeid=foodtypes[typeindex].typeid).childtypenames
    list = childtypename.split('#')
    chlist = []
    for i in list:
        list2 = i.split(':')
        dict1 = {'chname':list2[0],'chid':list2[1]}
        chlist.append(dict1)
    # print(chlist)

    if childid == '0':
        goodlist = Goods.objects.filter(categoryid=categoryid)
    else:
        goodlist = Goods.objects.filter(categoryid=categoryid, childcid=childid)


    # 排序
    if sortid == '1':  # 销量排序
        goodlist = goodlist.order_by('productnum')
    elif sortid == '2':  # 价格最低
        goodlist = goodlist.order_by('price')
    elif sortid == '3':  # 价格最高
        goodlist = goodlist.order_by('-price')


    token = request.session.get('token')
    carts = []
    if token:
        user = User.objects.get(token=token)
        carts = Cart.objects.filter(user=user).exclude(goodnumber=0)
        print(carts)
    data = {
        'title': '闪购超市',
        'foodtypes': foodtypes,
        'goodlist': goodlist,
        'categoryid': categoryid,
        'chlist': chlist,
        'childid': childid,
        'carts': carts
    }

    return render(request,'market.html',context=data)

# 购物车
def cart(request):
    token = request.session.get('token')

    if token:
        user = User.objects.get(token=token)
        carts = Cart.objects.filter(user=user).exclude(goodnumber=0)

    data = {
        'carts':carts
    }
    return render(request,'cart.html',context=data)

# 我的
def mine(request):
    token = request.session.get('token')

    data = {
        'title':'我的'
    }
    if token:
        user = User.objects.get(token=token)
        data['name'] = user.name
        data['rank'] = user.rank
        data['img'] = '/static/upfile/' + user.img
        data['login'] = True

    else:
        data['name'] = '未登录'
        data['rank'] = '无等级'
        data['img'] = '/static/upfile/axf.png'
        data['login'] = False

    return render(request,'mine.html',context=data)

# 注册
def register(request):
    if request.method == 'POST':
        # 获取注册信息写入数据库
        user = User()
        user.account = request.POST.get('account')
        user.password = encryption(request.POST.get('password'))
        user.name = request.POST.get('name')
        user.tel = request.POST.get('tel')
        user.address = request.POST.get('address')

        filepath = os.path.join(settings.MDEIA_ROOT,user.name + '.png')
        file = request.FILES.get('img')
        print(file)
        with open(filepath,'wb') as fp:
            for i in file.chunks():
                fp.write(i)

        user.img = user.name + '.png'

        user.token = str(uuid.uuid5(uuid.uuid4(),'register'))

        user.save()
        #添加状态持久
        request.session['token'] = user.token

        return redirect('axf:mine')

    elif request.method == 'GET':
        return render(request,'register.html')

# 密码加密
def encryption(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf_8'))
    return md5.hexdigest()

# 注销
def exit(request):

    # request.session.flush()

    logout(request)

    return redirect('axf:mine')

# 登录
def login(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')


        try:
            user = User.objects.get(account=account)
            if user.password == encryption(password):
                user.token = str(uuid.uuid5(uuid.uuid4(), 'login'))
                user.save()
                request.session['token'] = user.token
                return redirect('axf:mine')
            else:
                return render(request,'login.html',context={'error':'密码错误'})
        except:
            return render(request,'login.html',context={'error':'用户名错误'})
    elif request.method == 'GET':
        return render(request, 'login.html')

# 检查用户名(账号)
def checkacc(request):

    account = request.GET.get('account')

    try:
        user = User.objects.get(account=account)
        return JsonResponse({'message':'用户已存在','status':'-1'})
    except:
        return JsonResponse({'message':'用户名可用','status':'1'})

# 加入商品到购物车
def addtocart(request):
    goodid = request.GET.get('goodid')
    token = request.session.get('token')

    responseDate = {}

    if token:  #已登录
        user = User.objects.get(token=token)
        goods = Goods.objects.get(pk=goodid)
        carts = Cart.objects.filter(user=user).filter(goods=goods)

        if carts.exists():  #如果存在cart
            cart = carts.first()
            cart.goodnumber += 1
            # print(cart.goodnumber)
            if cart.goodnumber > int(goods.storenums):
                cart.goodnumber = goods.storenums
            cart.save()
            responseDate['msg'] = '添加到购物车成功'
            responseDate['status'] = '1'
            responseDate['number'] = cart.goodnumber
            return JsonResponse(responseDate)
        else:    #如果不存在cart,创建
            cart = Cart()
            cart.user = user
            cart.goods = goods
            cart.goodnumber = 1
            cart.save()

            responseDate['msg'] = '添加到购物车成功'
            responseDate['status'] = '1'
            responseDate['number'] = cart.goodnumber
            return JsonResponse(responseDate)

    else:
        responseDate['msg'] = '未登录'
        responseDate['status'] = '-1'
        return JsonResponse(responseDate)

# 从购物车删除商品
def subcart(request):
    token = request.session.get('token')
    goodid = request.GET.get('goodid')

    user = User.objects.get(token=token)
    goods = Goods.objects.get(pk=goodid)
    carts = Cart.objects.filter(user=user).filter(goods=goods)
    cart = carts.first()
    cart.goodnumber -= 1
    cart.save()

    responseDate = {
        'msg':'删除购物车商品成功',
        'status':'1',
        'number':cart.goodnumber
    }
    return JsonResponse(responseDate)

# 改变选中状态
def changeselectstatus(request):
    cartid = request.GET.get('cartid')
    print(cartid)
    cart = Cart.objects.get(pk=cartid)

    cart.isselect = not cart.isselect
    cart.save()
    responseDate = {
        'msg':'修改选中状态成功',
        'status':'1',
        'isselect':cart.isselect
    }
    return JsonResponse(responseDate)

# 全选/取消全选
def allselect(request):
    isall = request.GET.get('isall')
    if isall == 'false':
        isall = False
    elif isall == 'true':
        isall = True
    token = request.session.get('token')
    user = User.objects.get(token=token)
    carts = Cart.objects.filter(user=user)
    for cart in carts:
        cart.isselect = isall
        cart.save()

    responseDate = {
        'msg': '全选成功',
        'status': '1',
        'isselect': cart.isselect
    }
    return JsonResponse(responseDate)