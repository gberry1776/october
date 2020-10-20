from . import views
from django.conf.urls import url

app_name='experiment'

urlpatterns= [
    url(r'experiment/$',views.FirstView.as_view(),name='myrooms'),
    url(r'posts/in/(?P<slug>[-\w]+)/(?P<elnamo>[-\S]+)$',views.SingleGroup.as_view(),name='single1'),
    url(r'^$',views.ListGroups.as_view(),name='all1'),
    url(r'^new/$',views.CreateGroup.as_view(),name='create1'),
    url(r'join/(?P<slug>[-\S]+)/(?P<elnamo>[-\S]+)$',views.JoinGroup.as_view(),name='join1'),
    url(r'leave/(?P<slug>[-\S]+)/(?P<elnamo>[-\S]+)$',views.LeaveGroup.as_view(),name='leave1'),
    url(r'bjudge/(?P<slug>[-\w]+)/(?P<elnamo>[-\S]+)$',views.BecomeJudge.as_view(),name='bjudge1'),
    url(r'unjudge/(?P<slug>[-\w]+)/(?P<elnamo>[-\S]+)$',views.UnJudge.as_view(),name='unjudge1'),
    # url(r'fill/$',views.FillBoard.as_view(),name='FillBoard'),
    # url(r'^search/',views.solution.as_view(),name='solution')
]
