from django.shortcuts import reverse
from django.test import TestCase

from .classes import Favorite


class TestFavoriteClass(TestCase):
    def setUp(self):
        self.session = self.client.session
        self.session_key = 'TEST'
        self.favorite = Favorite(self.session, self.session_key)

    def test_init_favorite(self):
        self.assertEqual(self.favorite.session, self.session)

    def test_add_favorite(self):
        objects = [i for i in range(2)]
        for obj in objects:
            self.favorite.add(obj)
        self.assertEqual(self.session.get(self.session_key), f'[{objects[0]}, {objects[1]}]')

    def test_remove_favorite(self):
        objects = [_ for _ in range(4)]
        for obj in objects:
            self.favorite.add(obj)
        expected = f'[{objects[0]}, {objects[1]}, {objects[2]}, {objects[3]}]'
        self.assertEqual(self.session.get(self.session_key), expected)
        self.favorite.remove(objects[0])
        expected = f'[{objects[1]}, {objects[2]}, {objects[3]}]'
        self.assertEqual(self.session.get(self.session_key), expected)

    def test_clear_favorite(self):
        objects = [_ for _ in range(4)]
        for obj in objects:
            self.favorite.add(obj)
        expected = f'[{objects[0]}, {objects[1]}, {objects[2]}, {objects[3]}]'
        self.assertEqual(self.session.get(self.session_key), expected)
        self.favorite.clear()
        self.assertEqual(self.session.get(self.session_key), '[]')

    def test_serializable(self):
        objects = [_ for _ in range(3)]
        for obj in objects:
            self.favorite.add(obj)
        self.assertEqual(self.favorite.keys, [objects[0], objects[1], objects[2]])
        expected = f'[{objects[0]}, {objects[1]}, {objects[2]}]'
        self.assertEqual(self.favorite.serializable, expected)

    def test_count(self):
        objects = [_ for _ in range(3)]
        for obj in objects:
            self.favorite.add(obj)
        self.assertEqual(self.favorite.count, 3)


class TestFavoriteViews(TestCase):
    def setUp(self):
        self.session = self.client.session
        self.favorite = Favorite(self.session)

    def test_add_view(self):
        obj = 1
        response = self.client.post(reverse('favorite:add', kwargs={'pk': obj}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)
        self.assertEqual(response.json()['count'], 1)

    def test_remove_view(self):
        obj = 1
        self.favorite.add(obj)
        self.session.save()
        response = self.client.post(reverse('favorite:remove', kwargs={'pk': obj}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)
        self.assertEqual(response.json()['count'], 0)
