from django.conf.urls import url
from . import views


app_name='about'

urlpatterns= [
    url(r'aboutSu$',views.SuAbout.as_view(),name='aboutsu'),
    url(r'^general/$',views.GenAbout.as_view(),name='general'),
    url(r'^planet/$',views.PlanetAbout.as_view(),name='aboutpe')
]
