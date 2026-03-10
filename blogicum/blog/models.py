from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name='Заголовок')
    description = models.TextField(
        null=False,
        blank=False,
        verbose_name='Описание')
    slug = models.SlugField(
        null=False,
        blank=False,
        unique=True,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; '
        'разрешены символы латиницы, '
        'цифры, дефис и подчёркивание.')
    is_published = models.BooleanField(
        default=True,
        null=False,
        blank=False,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, '
        'чтобы скрыть публикацию.')
    created_at = models.DateTimeField(
    auto_now_add=True,
    null=False,
    blank=False,
    verbose_name='Добавлено')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(models.Model):
    name = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name='Название места')
    is_published = models.BooleanField(
        default=True,
        null=False,
        blank=False,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, '
        'чтобы скрыть '
        'публикацию.')
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
        verbose_name='Добавлено')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(models.Model):
    title = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name='Заголовок')
    text = models.TextField(
        null=False,
        blank=False,
        verbose_name='Текст')
    pub_date = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name='Дата и время публикации',
        help_text='Если установить '
        'дату и время в будущем '
        '— можно делать '
        'отложенные публикации.')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Автор публикации')
    location = models.ForeignKey(
        Location,
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        verbose_name='Местоположение')
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        blank=False,
        verbose_name='Категория')
    is_published = models.BooleanField(
        default=True,
        null=False,
        blank=False,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, '
        'чтобы скрыть публикацию.')
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
        verbose_name='Добавлено')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
