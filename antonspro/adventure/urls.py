from . import views
from django.conf.urls import url

app_name='adventure'

urlpatterns= [
    url(r'^$',views.start1.as_view(),name='start1'),
    url(r'^A2/$',views.A2.as_view(),name='A2'),
    ]
