from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='наименование категории')
    slug = models.SlugField(max_length=255, unique=True, null=False, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to='category/', default='category/avatar_default.jpeg',
                              verbose_name='изображение', **NULLABLE)

    def __str__(self):
        return f'Категория: {self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Subcategory(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='наименование подкатегории')
    slug = models.SlugField(max_length=255, unique=True, null=False, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to='subcategory/', default='subcategory/avatar_default.jpeg',
                              verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория',
                                 related_name='subcategory')

    def __str__(self):
        return f'Подкатегория: {self.title}'

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'


class Product(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='наименование продукта')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='подкатегория')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='цена')
    slug = models.SlugField(max_length=255, unique=True, null=False, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to='product/', default='product/avatar_default.jpeg',
                              verbose_name='изображение', **NULLABLE)

    def __str__(self):
        return f'Продукт: {self.title}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='изображение')

    def __str__(self):
        return f'Gallery: {self.product}'

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'
