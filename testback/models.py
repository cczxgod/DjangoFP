from django.db import models

class Product(models.Model):
    owner = models.CharField(max_length=30, blank=False)

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=60,blank=False)
    see_time = models.IntegerField(default=0)
    url = models.URLField(blank=False)
    products = models.ManyToManyField(Product, related_name="prodless")


class User(models.Model):
    name = models.CharField(max_length=20, blank=False)
    products = models.ManyToManyField(Product)
    lessons = models.ManyToManyField(Lesson, through="ListLes", related_name="userless")


class ListLes(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="listless")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listuser")
    time_viev = models.IntegerField(default=0)
    last_viev = models.DateField(default="2001-09-11")
    status = models.CharField(max_length=20,default="Не просмотрено")
