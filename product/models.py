from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, primary_key=True)

    def __str__(self):
        return  self.name

# варианты on_delete
# CASCADE - при удаление кагеории, удалятся все продукты из этой категории
# SET_NULL - при удалении категории, значение поля category для связанных продуктов будеть пустым (null)
# SET_DEFAULT - при удаление категории, значение поля category в связанных продуктов заменяется на дефолтное
# PROTECT - не дают удалить категорию, если в ней есть продукты
# RESTRICT - не дают удалить категорию, если в ней есть продукты
# DO_NOTHING - отсутствие действия

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return  self.title


# ORM (Object-Relational Mapping)
#TODO: Заполнить товары
#TODO: Сделать список товаров на сайте
#TODO: Добавить возможные загружать картинки товаров






