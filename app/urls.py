from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^checkuser/$', views.checkuser, name='checkuser'),
    url(r'^userlike/$', views.userlike, name='userlike'),

    url(r'^addlike/', views.addlike, name='addlike'),
    url(r'^sublike/', views.sublike, name='sublike'),

    #  用户信息修改
    url(r'^userinfo/$', views.userinfo, name='userinfo'),
]
