from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^market/(\d+)/(\d+)/(\d+)/', views.market,name='market'),
    url(r'^cart/', views.cart,name='cart'),
    url(r'^mine/', views.mine,name='mine'),
    url(r'^register/',views.register,name='register'),
    url(r'^logout/',views.exit,name='logout'),
    url(r'^login/',views.login,name='login'),
    url(r'^checkacc/',views.checkacc,name='checkacc'),
    url(r'^addtocart/',views.addtocart,name='addtocart'),
    url(r'^subcart/',views.subcart,name='subcart'),
    url(r'^changeselectstatus/',views.changeselectstatus,name='changeselectstatus'),
    url(r'^allselect/',views.allselect,name='allselect')
]