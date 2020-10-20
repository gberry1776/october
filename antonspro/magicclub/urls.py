from django.conf.urls import url

from . import views

app_name='magicclub'

urlpatterns= [
    url(r'^$',views.Homepage.as_view(),name='home'),
    url(r'tournament/(?P<slug>[-\w]+)/$',views.SingleGroup.as_view(),name='swiss'),
    url(r'pairings/(?P<slug>[-\w]+)/$',views.PairGroup.as_view(),name='pairings'),
    url(r'new/$',views.CreateGroup.as_view(),name='create'),
    url(r'all/$',views.ListGroups.as_view(),name='all'),
    url(r'standings/(?P<slug>[-\w]+)/$',views.StandingsGroup.as_view(),name='standings'),
    # url(r'by/(?P<username>[-\w]+)/$',views.UserPosts.as_view(),name='for_user'),
    # url(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.PostDetail.as_view(),name='single'),
    # url(r'delete/(?P<pk>\d+)/$',views.DeletePost.as_view(),name='delete')
]
