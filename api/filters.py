from .models import *
from django_filters.rest_framework import FilterSet, filters


class ProfileFilter(FilterSet):
    group = filters.CharFilter(field_name='group')
    division = filters.CharFilter(field_name='division', method='filter_by_division')
    course=filters.CharFilter(field_name='course',method='filter_by_coursename')

    class Meta:
        model = Profile
        fields = ['group']

    # 단대로 filtering
    def filter_by_division(self, queryset, name, value):

        pks = []
        filtered = Profile.objects.none()

        # Department테이블에서 특정 division에 해당하는 primary key들 가져오기
        for obj in Department.objects.all():
            if obj.division == value:
                pks.append(obj.id)  # 특정 division에 해당하는 id 들 모두 append

        pks=list(set(pks))

        for pk in pks:
            filtered = filtered | Profile.objects.filter(department_id=pk)

        return filtered

    # 특정 강좌에 등록한 학생들
    def filter_by_coursename(self, queryset, name, value):

        student_ids = []
        course_id = Course.objects.get(name=value).id

        for obj in Enrollment.objects.filter(course_id=course_id):
            student_ids.append(obj.student_id)

        filtered = Profile.objects.filter(id__in=student_ids)

        return filtered
