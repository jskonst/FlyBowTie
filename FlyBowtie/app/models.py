from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length = 50, verbose_name="Имя")
    last_name = models.CharField(max_length = 50, verbose_name="Фамилия")
    position = models.ForeignKey('Position', on_delete=models.CASCADE, verbose_name="Должность")
    class Meta(object):
        verbose_name_plural = "Люди"
        verbose_name = "человек"

    def __str__(self):
        return '{0} {1} | {2}'.format(self.first_name, self.last_name, self.position)

class Position(models.Model):
    name = models.CharField(max_length=50, unique=True ,verbose_name="Должность")
    class Meta(object):
        verbose_name_plural = "Должности"
        verbose_name = "должность"
    def __str__(self):
        return self.name