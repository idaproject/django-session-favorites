from .classes import Favorite


def add_favorites(request):
    ctx = dict()
    ctx['favorites'] = Favorite(request.session)
    return ctx
