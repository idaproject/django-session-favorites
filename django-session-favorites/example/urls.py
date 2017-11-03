# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^favorite/', include('session_favorites.urls', 'favorite')),
]
