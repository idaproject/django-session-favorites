from django.http import JsonResponse
from django.views.generic import View


class FavoriteAddView(View):
    # noinspection PyUnusedLocal
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            self.request.favorites.add(int(pk))
        except ValueError as err:
            return JsonResponse({'success': False, 'error': str(err)}, status=400)
        return JsonResponse({'success': True, 'count': self.request.favorites.count})


class FavoriteRemoveView(View):
    # noinspection PyUnusedLocal
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            self.request.favorites.remove(int(pk))
        except ValueError as err:
            return JsonResponse({'success': False, 'error': str(err)}, status=400)
        return JsonResponse({'success': True, 'count': self.request.favorites.count})
