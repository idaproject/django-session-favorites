from .classes import Favorite


class AddFavorites(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.favorites = Favorite(request.session)
        response = self.get_response(request)
        return response
