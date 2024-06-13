from django.urls import path
from ecommapp import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('cakes',views.cakes,name="cakes"),
    path('review',views.review,name="review"),
    path('contact',views.contact,name="contact"),
    path('choc',views.choc,name="choc"),
    path('vanila',views.vanila,name="vanila"),
    path('redvel',views.redvel,name="redvel"),
    path('bday',views.bday,name="bday"),
    path('wedd',views.wedd,name="wedd"),
    path('mtier',views.mtier,name="mtier"),
    path('signup',views.handlesignup,name="handlesignup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handlelogout,name="handlelogout")
]


