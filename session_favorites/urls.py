from django.conf.urls import url

from .views import FavoriteAddView, FavoriteRemoveView

urlpatterns = [
    url(r'^(?P<pk>[\d]+)/add/$', view=FavoriteAddView.as_view(), name='add'),
    url(r'^(?P<pk>[\d]+)/remove/$', view=FavoriteRemoveView.as_view(), name='remove'),
]