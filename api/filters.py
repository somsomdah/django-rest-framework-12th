from django.shortcuts import get_object_or_404
from django_filters.rest_framework import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import *

class ProfileFilter(FilterSet):
    name=filters.CharFilter(field_name='name',lookup_expr='icontains')
    group=filters.CharFilter(field_name='group')
    division=filters.CharFilter(field_name='division',method='filter_by_division')

    class Meta:
        model = Profile
        fields = ['name','group']

    # 단대로 filtering
    def filter_by_division(self,queryset,name,value):

        pks=[]
        filtered=Profile.objects.none()

        # Department테이블에서 특정 division에 해당하는 primary key들 가져오기
        for obj in Department.objects.all():
            if obj.division==value:
                pks.append(obj.id) # 특정 division에 해당하는 id 들 모두 append

        for pk in pks:
            filtered=filtered|Profile.objects.filter(department_id=pk)

        return filtered






