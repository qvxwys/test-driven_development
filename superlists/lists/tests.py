from django.test import TestCase

from lists.models import Item


class HomePageTest(TestCase):
    """Тест домашней страницы."""

    def test_uses_home_template(self):
        """Тест: используется домашний шаблон."""

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        """Тест: можно сохранить post-запрос."""

        # выполняем POST-запрос, принимающий аргумент data с данными формы,
        # которые мы хотим отправить
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
        # удостоверяемся, что текст из POST-запроса появляется в HTML
        self.assertIn('A new list item', response.content.decode())
        # проверка, что используется шаблон
        self.assertTemplateUsed(response, 'home.html')

    def test_only_saves_items_when_necessary(self):
        """Тест: сохраняет элементы, только когда нужно."""
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):
    """Тест модели элемента списка."""

    def test_saving_and_retrieving_items(self):
        """Тест сохранения и получения элементов списка."""
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
