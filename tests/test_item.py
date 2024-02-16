import pytest
from src.item import Item
from src.phone import Phone
from config import ITEMS
from src.item import InstantiateCSVError

"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_add(item, phone):
    assert phone + item == 25


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_items(item):
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000.0


def test_name(item):
    """Тест проверки длины наименования товара(не больше 10 символов"""
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"
    item1.name = "Духовой шкаф"
    assert item1.name == "Духовой шк"


def test_instantiate_from_csv():
    """Проверка добавления экземпляров класса из CSV файла"""
    Item.instantiate_from_csv(ITEMS)
    assert len(Item.all) == 5


def test_string_to_number():
    """Проверка возвращения числа из строки-числа"""
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("1.5") == 1


def test_repr():
    """тест для метода repr"""
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str(item):
    """тест для метода str"""
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == "Смартфон"


def test_instantiate_from_csv_not():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('path.csv')


def test_instantiate_from_csv_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('items.csv')
