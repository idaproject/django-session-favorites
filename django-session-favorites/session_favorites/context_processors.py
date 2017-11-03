from apps.favorites.classes import Favorite


def add_favorite(request):
    ctx = dict()
    ctx['favorite'] = Favorite(request.session)
    return ctx
