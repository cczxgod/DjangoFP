from rest_framework import serializers

from .models import Lesson, User, Product, ListLes


class Stats:
    def __init__(self, ow, cv, tv, cu, bp):
        self.owner = ow
        self.count_view = cv
        self.time_view = tv
        self.count_users = cu
        self.buy_percent = bp


class ListLesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListLes
        fields = ['status', 'time_viev', 'last_viev']


class ProductSerr(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ListSerr(serializers.ModelSerializer):
    listless = ListLesSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ['lesson_name', 'see_time', 'listless']


class LessSer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['lesson_name']


class ListLessSerializer(serializers.ModelSerializer):
    lesson = LessSer(read_only=True)

    class Meta:
        model = ListLes
        fields = ['lesson', 'status', 'time_viev']



class ProductList(serializers.ModelSerializer):
    lessons = ListSerr(many=True, read_only=True)
    name = serializers.CharField()

    class Meta:
        model = User
        fields = ['name', 'lessons']


class LessonList(serializers.ModelSerializer):
    lesson = ListSerr(read_only=True)

    class Meta:
        model = ListLes
        fields = ['status','lesson','time_viev']


class StatSer(serializers.Serializer):
    owner = serializers.CharField()
    count_view = serializers.IntegerField()
    time_view = serializers.IntegerField()
    count_users = serializers.IntegerField()
    buy_percent = serializers.FloatField()