from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Prefetch

from .serializers import ListLessSerializer, ProductList, LessonList, StatSer, Stats, ProductSerr
from .models import ListLes, Product, Lesson, User

# Create your views here.
class ListLessonsAPI(APIView):
    def get(self, request):
        lst = ListLes.objects.filter(user_id=request.GET.get('user_id')).select_related('lesson')
        return Response({'LessonUsers': ListLessSerializer(lst, many=True).data})


class ProductLessonAPI(APIView):
    def get(self, request):
        lst = Lesson.objects.prefetch_related(Prefetch('listless', queryset=ListLes.objects.filter(user_id=request.GET.get('user_id')).select_related('lesson'))).filter(products=request.GET.get('product_id'))
        ls1 = User.objects.filter(id=request.GET.get('user_id')).prefetch_related(Prefetch('lessons', queryset=lst))
        return Response({'LessonsProduct': ProductList(ls1, many=True).data})

class StatisticAPI(APIView):
    def get(self, request):
        temp = ProductSerr(Product.objects.all(), many=True).data
        tmpl = []
        for j in range(len(temp)):
            lst = ListLes.objects.prefetch_related(Prefetch('lesson',
                queryset=Lesson.objects.prefetch_related(Prefetch('products',
                queryset=Product.objects.all())))).filter(lesson__products=temp[j].get('id')).filter(status='Просмотрено')
            count = len(lst)
            tw=0
            a = LessonList(lst, many=True).data
            for i in range(len(a)):
                tw += a[i].get('time_viev')
            owner = temp[j].get('owner')
            ls1 = User.objects.prefetch_related('products').filter(products =temp[j].get('id'))
            count_users = len(ls1)
            print(count_users)
            ls2 = User.objects.all()
            percent = count_users / len(ls2) * 100
            print(percent)
            statistic = Stats(owner,count, tw, count_users, percent)
            tmpl.append(statistic)
        return Response({'Products': StatSer(tmpl, many=True).data})