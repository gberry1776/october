"""antonspro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf.urls import url,include


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^Home/$',views.HomePage.as_view(),name='home'),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^test/$',views.TestPage.as_view(),name='test'),
    url(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
    url(r'^posts/',include('posts.urls',namespace='posts')),
    url(r'^groups/',include('groups.urls',namespace='groups')),
    url(r'^$',views.MasterPage.as_view(),name='masterpage'),
    url(r'^sudoku/',include('sudoku.urls',namespace='sudoku')),
    url(r'^about/',include('about.urls',namespace='about')),
    url(r'^experiment/',include('experiment.urls',namespace='experiment')),
    url(r'^buy/$',views.BuyPage.as_view(),name='buy'),
    url(r'^magicclub/',include('magicclub.urls',namespace='magicclub')),
    url(r'^adventure/',include('adventure.urls',namespace='adventure')),
]
