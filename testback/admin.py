from django.contrib import admin

from .models import User, Lesson, Product, ListLes

admin.site.register(User)
admin.site.register(Lesson)
admin.site.register(Product)
admin.site.register(ListLes)

