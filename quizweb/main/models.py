from django.db import models
from django.contrib.auth.models import User


class Word(models.Model):
    original = models.CharField('Оригинал', max_length=100)
    meaning = models.CharField('Перевод', max_length=100)

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"

    def __str__(self):
        return self.original


class Question(models.Model):
    word = models.ForeignKey('Word', on_delete=models.CASCADE, verbose_name='Слово')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    option1 = models.CharField('Вариант 1', max_length=100)
    option2 = models.CharField('Вариант 2', max_length=100)
    option3 = models.CharField('Вариант 3', max_length=100)
    correct_option = models.CharField('Верный ответ', max_length=100)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return f"Вопрос о {self.word.original}"


class Category(models.Model):
    name = models.CharField('Категория', max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    score = models.IntegerField('Балл')

    class Meta:
        verbose_name = "Балл"
        verbose_name_plural = "Баллы"

    def __str__(self):
        return f"{self.score}"

