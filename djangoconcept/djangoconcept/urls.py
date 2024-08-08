"""
URL configuration for djangoconcept project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from conceptapp import views

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', views.home_view,name="home"),
    path('recview/',views.fvb_rec_view),
    path('addrec/',views.fbv_add),
    path('delrec/<int:id>/',views.fbv_del),
    path('updaterec/<int:id>/',views.fbv_update),
    path('cbvrecview/',views.stdrec_view.as_view(),name='recview'),
    path('cbvaddrec/',views.stdadd_view.as_view()),
    path('cbvdetailrec/<int:pk>',views.stdDetail_view.as_view(),name="cbvrec"),
    path('cbvupdaterec/<int:pk>',views.stdupdate_view.as_view()),
    path('cbvdelrec/<int:pk>',views.stddel_view.as_view()),
    path('product/',views.product_view),
    path('customer/',views.customer_view,name='customer'),
    path('preview/',views.preview,name="preview"),
    path('validate/',views.Validation_view),
    path('logup/',views.logup_view),
    path('login/',views.login_view),
    path('logout/',views.logout_view),
    path('profile/',views.profile_view),
    path('orm/',views.orm_view),
    path('productslist/',views.cookie_view),
    path('cart/',views.cart_view),
    path('res/',views.result_view),
    path('srec/',views.search_rec,name="srec"),
    path('filter/',views.filter_view),

]
