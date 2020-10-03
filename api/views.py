from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework import status,response

# Create your views here.

'''profile'''
# api/profile/
class ProfileList(APIView): #APIView 상속

    # Profile 추가
    def post(self,request):
        serializer=ProfileSerializer(data=request.data) # serializer.data에 request.data 추가
        if serializer.is_valid():
            serializer.save() # 저장 : profile database에 반영됨
            return response.Response(serializer.data,status=status.HTTP_201_CREATED) # 모든 profile을 json 형태로 응답
        else:
            return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # 모든 Profile 조회
    def get(self, request): #모든 사용자 조회
        queryset=Profile.objects.all() # 모든 profile 쿼리셋 반환
        serializer=ProfileSerializer(queryset,many=True) # queryset serialize
        return response.Response(serializer.data) # serialization 결과인 serializer.data(json)으로 응답

# api/profile/pk
class ProfileDetail(APIView):

    # 특정 Profile 조회
    def get(self,request,pk):
        profile=Profile.objects.get(pk=pk) # Profile 인스턴스 반환
        serializer=ProfileSerializer(profile) # Profile 인스턴스 serialize
        return response.Response(serializer.data) # json 형태인 serializer.data로 응답

    # 특정 Profile 수정
    def put(self,request,pk):
        profile=Profile.objects.get(pk=pk)
        serializer=ProfileSerializer(profile,data=request.data) # profile 인스턴스를 serealize 후 request.data로 변경
        if serializer.is_valid():
            serializer.save() # 저장 : database에 반영됨
            return response.Response(serializer.data) # 변경된 데이터로 응답
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 특정 Profile 제거
    def delete(self,request,pk):
        profile=Profile.objects.get(pk=pk) # 특정 profile 인스턴스를 받아서
        profile.delete() # 삭제
        return response.Response(status=status.HTTP_204_NO_CONTENT)


'''Department'''
class DepartmentList(APIView):
    def post(self,request):
        serializer=DepartmentSerializer(data=request.data)
        serializer.save()
        return response(serializer.data,status=status.HTTP_201_CREATED)

    def get(self,request):
        queryset=Department.objects.all()
        serializer=DepartmentSerializer(queryset,many=True)
        return response.Response(serializer.data)

class DepartmentDetail(APIView):
    def get(self,request,pk):
        department=Department.objects.get(pk=pk)
        serializer=DepartmentSerializer(department)
        return response.Response(serializer.data)

    def put(self,request,pk):
        department=Department.objects.get(pk=pk)
        serializer=DepartmentSerializer(department,data=request.data)
        serializer.save()
        return response.Response(serializer.data)

    def delete(self,request,pk):
        department = Department.objects.get(pk=pk)
        department.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

'''Course'''
class CourseList(APIView):
    def post(self,request):
        serializer=CourseSerializer(data=request.data)
        serializer.save()
        return response(serializer.data,status=status.HTTP_201_CREATED)

    def get(self,request):
        queryset=Course.objects.all()
        serializer=CourseSerializer(queryset,many=True)
        return response.Response(serializer.data)

class CourseDetail(APIView):
    def get(self,request,pk):
        course=Course.objects.get(pk=pk)
        serializer=CourseSerializer(course)
        return response.Response(serializer.data)

    def put(self,request,pk):
        course=Course.objects.get(pk=pk)
        serializer=CourseSerializer(course,data=request.data)
        serializer.save()
        return response.Response(serializer.data)

    def delete(self,request,pk):
        course = Course.objects.get(pk=pk)
        course.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


'''Major'''
class MajorList(APIView):
    def post(self,request):
        serializer=MajorSerializer(data=request.data)
        serializer.save()
        return response(serializer.data,status=status.HTTP_201_CREATED)

    def get(self,request):
        queryset=Major.objects.all()
        serializer=MajorSerializer(queryset,many=True)
        return response.Response(serializer.data)

class MajorDetail(APIView):
    def get(self,request,pk):
        major=Major.objects.get(pk=pk)
        serializer=MajorSerializer(major)
        return response.Response(serializer.data)

    def put(self,request,pk):
        major=Major.objects.get(pk=pk)
        serializer=MajorSerializer(major,data=request.data)
        serializer.save()
        return response.Response(serializer.data)

    def delete(self,request,pk):
        major = Major.objects.get(pk=pk)
        major.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)



'''MajorIn'''

class MajorInList(APIView):
    def post(self,request):
        serializer=MajorInSerializer(data=request.data)
        serializer.save()
        return response(serializer.data,status=status.HTTP_201_CREATED)

    def get(self,request):
        queryset=MajorIn.objects.all()
        serializer=MajorInSerializer(queryset,many=True)
        return response.Response(serializer.data)

class MajorInDetail(APIView):
    def get(self,request,pk):
        majorin=MajorIn.objects.get(pk=pk)
        serializer=MajorInSerializer(majorin)
        return response.Response(serializer.data)

    def put(self,request,pk):
        majorin=MajorIn.objects.get(pk=pk)
        serializer=MajorInSerializer(majorin,data=request.data)
        serializer.save()
        return response.Response(serializer.data)

    def delete(self,request,pk):
        majorin = MajorIn.objects.get(pk=pk)
        majorin.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)



'''Enrollment'''

class EnrollmentList(APIView):
    def post(self,request):
        serializer=EnrollmentSerializer(data=request.data)
        serializer.save()
        return response(serializer.data,status=status.HTTP_201_CREATED)

    def get(self,request):
        queryset=Enrollment.objects.all()
        serializer=EnrollmentSerializer(queryset,many=True)
        return response.Response(serializer.data)

class EnrollmentDetail(APIView):
    def get(self,request,pk):
        enrollment=Enrollment.objects.get(pk=pk)
        serializer=EnrollmentSerializer(enrollment)
        return response.Response(serializer.data)

    def put(self,request,pk):
        enrollment=Enrollment.objects.get(pk=pk)
        serializer=EnrollmentSerializer(enrollment,data=request.data)
        serializer.save()
        return response.Response(serializer.data)

    def delete(self,request,pk):
        enrollment = Enrollment.objects.get(pk=pk)
        enrollment.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)







