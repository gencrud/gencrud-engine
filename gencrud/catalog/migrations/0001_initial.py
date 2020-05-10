# Generated by Django 2.2.7 on 2020-05-09 16:40

import ckeditor_uploader.fields
from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields
import gen.utils.url
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('site_info', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('param', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, default='заголовок объекта', max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('html', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='HTML/Текст')),
                ('is_show', models.BooleanField(default=True, verbose_name='Отображать')),
                ('sort', models.SmallIntegerField(default=1000, help_text='<br><i>\nЛучше использовать за единицу сортировки 1000 или 100.. \nТак проще будет разобраться, если элементы имеют большую вложенность.<br>\nИли придумайте свою систему сортировки : )\n<br>ПРИМЕР - 1000:__________________ПРИМЕР - 2000:\n<br>.... Пример - 1100__________________.... Пример - 2200\n<br>........... пример - 1110__________________........ пример - 2220\n<br>............... пример - 1111__________________............... пример - 2222</i>\n', verbose_name='Сортировка')),
                ('is_allow_comments', models.BooleanField(default=False, verbose_name='разрешить комментарии')),
                ('slug', models.SlugField(help_text='генерируется автоматически', verbose_name='элемент URL')),
                ('seo_title', models.CharField(blank=True, help_text='Предпочтительное значение 50-80 символов', max_length=255, null=True, verbose_name='Seo title')),
                ('seo_description', models.TextField(blank=True, help_text='Предпочтительное значение 150-200 символов', max_length=510, null=True, verbose_name='Seo description')),
                ('seo_keywords', models.TextField(blank=True, help_text='Ориентируйтесь на ударные первые 150 знаков, 250 максимум', max_length=510, null=True, verbose_name='Seo keywords')),
                ('og_locale', models.TextField(blank=True, default='ru_RU', help_text='\nгруппа мета-тегов, рассказывающая социальным сетям о содержимом страниц, которыми вы делитесь.\nБлагодаря этому ссылки из набора символов превращаются в понятные заголовки с картинками и пояснениями.\n<code>\n    <meta property="og:url" content="http://www.mysite.ru/2015/02/19/arts/international/page.html" />\n    <meta property="og:type" content="article" />\n    <meta property="og:title" content="When Great Minds Don’t Think Alike" />\n    <meta property="og:description" content="How much does culture influence creative thinking?" />\n    <meta property="og:image" content="http://mysite.com/static/img/2015/02/19/img.jpg" />\n</code>\n', max_length=510, null=True, verbose_name='og locale')),
                ('scripts', models.TextField(blank=True, help_text='\nПример: "Подключение CSS фрэймворка - Bootstrap 4.0"<br>\n--------------------------------------------------------<br> \n< script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script><br>\n< script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script><br>\n< script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>\n', null=True, verbose_name='Блок скриптов')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обнавлен')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subitems', to='catalog.Catalog', verbose_name='Родительский объект')),
                ('tags', models.ManyToManyField(blank=True, to='site_info.Tag', verbose_name='Тэги')),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталог',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, default='заголовок объекта', max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('name', models.CharField(blank=True, max_length=512, null=True, verbose_name='Расшифровка')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Цена')),
                ('unit', models.CharField(choices=[('pcs', 'шт.'), ('m', 'п.м'), ('sqm', 'м.кв'), ('cbm', 'м.куб'), ('not_show', ' - ')], default='pcs', max_length=3, verbose_name='Ед.изм')),
            ],
            options={
                'verbose_name': 'Прайс',
                'verbose_name_plural': 'Прайс',
                'ordering': ('title', 'price'),
                'abstract': False,
                'unique_together': {('title', 'name', 'price', 'unit')},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, default='заголовок объекта', max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('html', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='HTML/Текст')),
                ('is_show', models.BooleanField(default=True, verbose_name='Отображать')),
                ('sort', models.SmallIntegerField(default=1000, help_text='<br><i>\nЛучше использовать за единицу сортировки 1000 или 100.. \nТак проще будет разобраться, если элементы имеют большую вложенность.<br>\nИли придумайте свою систему сортировки : )\n<br>ПРИМЕР - 1000:__________________ПРИМЕР - 2000:\n<br>.... Пример - 1100__________________.... Пример - 2200\n<br>........... пример - 1110__________________........ пример - 2220\n<br>............... пример - 1111__________________............... пример - 2222</i>\n', verbose_name='Сортировка')),
                ('is_allow_comments', models.BooleanField(default=False, verbose_name='разрешить комментарии')),
                ('slug', models.SlugField(help_text='генерируется автоматически', verbose_name='элемент URL')),
                ('seo_title', models.CharField(blank=True, help_text='Предпочтительное значение 50-80 символов', max_length=255, null=True, verbose_name='Seo title')),
                ('seo_description', models.TextField(blank=True, help_text='Предпочтительное значение 150-200 символов', max_length=510, null=True, verbose_name='Seo description')),
                ('seo_keywords', models.TextField(blank=True, help_text='Ориентируйтесь на ударные первые 150 знаков, 250 максимум', max_length=510, null=True, verbose_name='Seo keywords')),
                ('og_locale', models.TextField(blank=True, default='ru_RU', help_text='\nгруппа мета-тегов, рассказывающая социальным сетям о содержимом страниц, которыми вы делитесь.\nБлагодаря этому ссылки из набора символов превращаются в понятные заголовки с картинками и пояснениями.\n<code>\n    <meta property="og:url" content="http://www.mysite.ru/2015/02/19/arts/international/page.html" />\n    <meta property="og:type" content="article" />\n    <meta property="og:title" content="When Great Minds Don’t Think Alike" />\n    <meta property="og:description" content="How much does culture influence creative thinking?" />\n    <meta property="og:image" content="http://mysite.com/static/img/2015/02/19/img.jpg" />\n</code>\n', max_length=510, null=True, verbose_name='og locale')),
                ('scripts', models.TextField(blank=True, help_text='\nПример: "Подключение CSS фрэймворка - Bootstrap 4.0"<br>\n--------------------------------------------------------<br> \n< script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script><br>\n< script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script><br>\n< script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>\n', null=True, verbose_name='Блок скриптов')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обнавлен')),
                ('articul', models.CharField(blank=True, db_index=True, max_length=256, null=True, verbose_name='Артикул (уник)')),
                ('is_bestseller', models.BooleanField(default=False, verbose_name='Хит продаж')),
                ('is_new', models.BooleanField(default=True, verbose_name='Новинка')),
                ('layout', models.CharField(choices=[('product/templates/product_detail.html', 'Шаблон по умолчанию'), ('product/templates/product_detail_layout_images_min_bottom.html', 'Шаблон: мини-изображения под главной фотографией')], default='product/templates/product_detail.html', max_length=256, verbose_name='Шаблоны страницы')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('catalogs', models.ManyToManyField(blank=True, limit_choices_to={'is_show': True}, to='catalog.Catalog', verbose_name='Каталог')),
                ('recommend_products', models.ManyToManyField(blank=True, help_text='Отображаются внизу карточки товара, как рекомендованные или похожие товары', limit_choices_to={'is_show': True}, related_name='_product_recommend_products_+', to='catalog.Product', verbose_name='Рекомендованные/Похожие')),
                ('tags', models.ManyToManyField(blank=True, to='site_info.Tag', verbose_name='Тэги')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'abstract': False,
                'unique_together': {('title', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='ProductParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str_value', models.CharField(blank=True, max_length=255, null=True, verbose_name='Значение(строка)')),
                ('int_value', models.IntegerField(blank=True, null=True, verbose_name='Значение(целое число)')),
                ('decimal_value', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, verbose_name='Значение(денежный формат)')),
                ('bool_value', models.NullBooleanField(max_length=255, verbose_name='Значение(булево)')),
                ('param', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='param.Param', verbose_name='Параметр')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар:параметры',
                'verbose_name_plural': 'Товар:параметры',
                'ordering': ('product', 'param'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to=gen.utils.url.generate_path_year_month, verbose_name='Изображение')),
                ('image_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название фото')),
                ('image_is_main', models.BooleanField(default=False, help_text='Главным может быть только одно фото', verbose_name='Главное')),
                ('image_description', models.TextField(blank=True, null=True, verbose_name='Краткое описание фото')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар:фото',
                'verbose_name_plural': 'Товар:фото',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обнавлен')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('ip_address', models.GenericIPAddressField(default='0.0.0.0', null=True, verbose_name='IP address')),
                ('username', models.CharField(blank=True, default='anonymous', max_length=125, null=True, verbose_name='Имя пользователя')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('is_show', models.BooleanField(default=False, verbose_name='Отображать')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Product', verbose_name='Товар:коментарий')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Товар:коментарий',
                'verbose_name_plural': 'Товар:коментарии',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CatalogImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to=gen.utils.url.generate_path_year_month, verbose_name='Изображение')),
                ('image_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название фото')),
                ('image_is_main', models.BooleanField(default=False, help_text='Главным может быть только одно фото', verbose_name='Главное')),
                ('image_description', models.TextField(blank=True, null=True, verbose_name='Краткое описание фото')),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Catalog', verbose_name='Каталог')),
            ],
            options={
                'verbose_name': 'Каталог:фото',
                'verbose_name_plural': 'Каталог:фото',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обнавлен')),
                ('name', models.CharField(max_length=512, verbose_name='Наименование')),
                ('text', models.CharField(blank=True, max_length=510, null=True, verbose_name='Дополнительно')),
                ('unit', models.CharField(choices=[('pcs', 'шт.'), ('m', 'п.м'), ('sqm', 'м.кв'), ('cbm', 'м.куб'), ('not_show', ' - ')], default='pcs', max_length=3, verbose_name='Ед.изм')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Цена')),
                ('price_discount', models.DecimalField(blank=True, decimal_places=2, help_text='Если указана - станет `Ценой` товара', max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Акционная цена')),
                ('is_main', models.BooleanField(default=False, verbose_name='Главный')),
                ('default_price', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Price', verbose_name='Взять из прайса')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар:вариант',
                'verbose_name_plural': 'Товар:варианты',
                'ordering': ('product', '-is_main', 'name'),
                'abstract': False,
                'unique_together': {('product', 'name')},
            },
        ),
    ]
