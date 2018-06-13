urlpatterns = [
    url(r'^$', views.index),
    url(r'^([0-9]+)/$', views.best),
]