import hashlib

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app.models import User, Banner, Movies, Like


# 主页
# TODO 存在一定问题,(缓存或者是try的问题)
def home(request):
    username = request.session.get('username')
    data = {
        'title': '微电影',
    }
    # 加载banner图
    banners = Banner.objects.all()
    data['banners'] = banners
    # 加载电影
    movies = Movies.objects.all()
    data['movies'] = movies
    try:
        # 登录注册的显示
        if username:
            user = User.objects.filter(u_name=username).first()
            data['username'] = username
            data['islogin'] = 'login'
            data['icon'] = user.u_icon.url
    except Exception as e:
        print(e)
    return render(request, 'app/home/home.html', context=data)


# 注册页面
def register(request):
    # 使用的是聚合，通过表单的method来判断
    if request.method == 'POST':
        # 获取到提交的数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('u_email')
        print(password, '\n', email, '\n', username)
        # repassword = request.POST.get('repassword')
        icon = request.FILES.get('icon')

        user = User()
        user.u_name = username
        password = password2md5(password)
        print('摘要后', password)
        user.u_password = password
        user.u_icon = icon
        user.email = email
        user.save()
        print('用户注册成功')
        #     设置session缓存
        request.session['username'] = username
        response = redirect(reverse('app:home'))
        return response
    elif request.method == 'GET':
        return render(request, 'app/home/register.html')


# md5摘要
def password2md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


# ajax用户检测
def checkuser(request):
    username = request.GET.get('username')
    users = User.objects.filter(u_name=username)
    print('检测用户名')
    data = {
        'msg': '用户名可用',
        'status': '888'
    }
    if users.exists():
        data['msg'] = '用户名已存在'
        data['status'] = '900'
    return JsonResponse(data)


# 登录
def login(request):
    print('123:', type(request.POST.get('email_flag')))
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        if request.POST.get('email_flag') == '1':
            users = User.objects.filter(isDelete=False).filter(email=username)
        else:
            users = User.objects.filter(isDelete=False).filter(u_name=username)

        if users.exists():
            user = users.first()
            u_password = user.u_password
            password = password2md5(password)
            if u_password == password:
                request.session['username'] = user.u_name
                return redirect(reverse('app:home'))
        return render(request, 'app/home/login.html', {'testlogin': '用户名或密码错误'})
    elif request.method == 'GET':
        return render(request, 'app/home/login.html')


# TODO 重复判断没有写,存在一个能收藏两次,暂时不做调整
def addlike(request):
    username = request.session.get('username')
    data = {
        'status': '200',
        'msg': 'ok',
    }
    if not username:
        data['status'] = '302'
        data['msg'] = '用户未登录'
        print('用户未登录')
        return JsonResponse(data)
    postid = request.GET.get('postid')
    print(postid)
    movie = Movies.objects.filter(postid=postid).first()
    like = Like()
    like.like_user = User.objects.filter(u_name=username).first()
    like.like_movies = movie
    # user = User.objects.filter(u_name=username).first()
    # if movie.is_like:
    #     # movie.is_like = False
    #     movie.like_num -= 1
    #     movie.save()
    # else:
    # movie.is_like = True
    like.save()
    movie.like_num += 1
    movie.save()
    data['num'] = movie.like_num
    return JsonResponse(data)


# 个人信息页面
def userinfo(request):
    username = request.session.get('username')
    if request.method == 'POST':
        users = User.objects.filter(u_name=username)

        if users.exists():
            user = users.first()
            q_email = request.POST.get('email')
            if q_email != '':
                user.email = q_email

            # print()
            q_icon = request.FILES.get('icon')
            print(q_icon, q_icon)
            if q_icon != None:
                user.u_icon = q_icon

            user.save()
            # print(user.u_icon)
            print('postpostpost')
            resp = redirect(reverse('app:home'))
            return resp
    elif request.method == 'GET':
        print(username)
        # user = User.objects.filter(u_name=username).first()
        user = User.objects.filter(u_name=username).first()
        print(user.u_name)
        print(user.u_icon)
        data = {
            'user': user,
        }
        return render(request, 'app/home/userinfo_mod.html', data)


# 退出
def logout(request):
    request.session.flush()
    return redirect(reverse('app:home'))


# TODO 偷懒偷懒
def userlike(request):
    username = request.session.get('username')
    data = {
        'title': '微电影',
    }
    # 加载banner图
    banners = Banner.objects.all()
    data['banners'] = banners
    # 加载电影
    user = User.objects.filter(u_name=username).first()

    movies = Like.objects.filter(like_user=user)

    data['movies'] = movies
    try:
        # 登录注册的显示
        if username:
            user = User.objects.filter(u_name=username).first()
            data['username'] = username
            data['islogin'] = 'login'
            data['icon'] = user.u_icon.url
    except Exception as e:
        print(e)
    return render(request, 'app/home/home_logined_collected.html', context=data)


# TODO 存在一定问题
def sublike(request):
    username = request.session.get('username')
    data = {
        'status': '200',
        'msg': 'ok',
    }
    if not username:
        data['status'] = '302'
        data['msg'] = '用户未登录'
        print('用户未登录')
        return JsonResponse(data)
    postid = request.GET.get('postid')
    print(postid)
    movie = Movies.objects.filter(postid=postid).first()
    like = Like.objects.filter(like_movies=movie).first()
    like.delete()
    return JsonResponse(data)
