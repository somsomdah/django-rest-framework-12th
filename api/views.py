from .serializers import *
from rest_framework.views import APIView
from rest_framework import status,response

# Create your views here.

'''User'''
# api/user/
class UserList(APIView): #APIView 상속

    # 사용자 추가
    def post(self,request):
        serializer=UserSerializer(data=request.data) # 요청 데이터를 받아서 serialize
        if serializer.is_valid():
            serializer.save() # 저장 : desrialization 후 user database에 반영됨
            return response.Response(serializer.data,status=status.HTTP_201_CREATED) # json으로 응답
        else:
            return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # 모든 사용자 조회
    def get(self, request): #모든 사용자 조회
        queryset=User.objects.all()
        serializer=UserSerializer(queryset,many=True) #quaryset을 json으로
        return response.Response(serializer.data) # serialization 결과인 json으로 응답

# api/user/pk
class UserDetail(APIView):

    # 특정 사용자 조회
    def get(self,request,pk):
        user=User.objects.get(pk=pk)
        serializer=UserSerializer(user) #인스턴스->json (serialize)
        return response.Response(serializer.data)

    # 특정 사용자정보 수정
    def put(self,request,pk):
        user=User.objects.get(pk=pk)
        serializer=UserSerializer(user,data=request.data) #user 인스턴스를 serealize 후 request.data로 변경
        if serializer.is_valid():
            serializer.save() # 저장 -> deserialization 후 database에 반영됨
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 특정 사용자 제거
    def delete(self,request,pk):
        user=User.objects.get(pk=pk) # 특정 user 인스턴스를 받아서
        user.delete() # 삭제
        return response.Response(status=status.HTTP_204_NO_CONTENT)


'''Department'''
class DepartmentList(APIView):
    def post(self,request):
        serializer=DepartmentSerializer(data=request.data)
        serializer.save()
        response(serializer.data,status=status.HTTP_201_CREATED)

    def get(self,request):
        queryset=Department.objects.all()
        serializer=DepartmentSerializer(queryset,many=True)
        response.Response(serializer.data)

class DepartmentDetail(APIView):
    def get(self,request,pk):
        department=Department.object.get(pk=pk)
        serializer=DepartmentSerializer(department)
        return response.Response(serializer.data)

    def put(self,request,pk):
        department=Department.objects.get(pk=pk)
        serializer=DepartmentSerializer(department,data=request.data)
        serializer.save()
        response.Response(serializer.data)

    def delete(self,request,pk):
        department = Department.objects.get(pk=pk)
        department.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

'''Course'''
class CourseList(APIView):
    def post(self,request):
        serializer=CourseSerializer(data=request.data)
        serializer.save()
        response(serializer.data,status=status.HTTP_201_CREATED)

    def get(self,request):
        queryset=Course.objects.all()
        serializer=CourseSerializer(queryset,many=True)
        response.Response(serializer.data)

class CourseDetail(APIView):
    def get(self,request,pk):
        course=Course.object.get(pk=pk)
        serializer=CourseSerializer(course)
        return response.Response(serializer.data)

    def put(self,request,pk):
        course=Course.objects.get(pk=pk)
        serializer=CourseSerializer(course,data=request.data)
        serializer.save()
        response.Response(serializer.data)

    def delete(self,request,pk):
        course = Course.objects.get(pk=pk)
        course.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


'''Major'''
class MajorList(APIView):
    def post(self,request):
        serializer=MajorSerializer(data=request.data)
        serializer.save()
        response(serializer.data,status=status.HTTP_201_CREATED)

    def get(self,request):
        queryset=Major.objects.all()
        serializer=MajorSerializer(queryset,many=True)
        response.Response(serializer.data)

class MajorDetail(APIView):
    def get(self,request,pk):
        major=Major.object.get(pk=pk)
        serializer=MajorSerializer(major)
        return response.Response(serializer.data)

    def put(self,request,pk):
        major=Major.objects.get(pk=pk)
        serializer=MajorSerializer(major,data=request.data)
        serializer.save()
        response.Response(serializer.data)

    def delete(self,request,pk):
        major = Major.objects.get(pk=pk)
        major.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)



'''MajorIn'''

class MajorInList(APIView):
    def post(self,request):
        serializer=MajorInSerializer(data=request.data)
        serializer.save()
        response(serializer.data,status=status.HTTP_201_CREATED)

    def get(self,request):
        queryset=MajorIn.objects.all()
        serializer=MajorInSerializer(queryset,many=True)
        response.Response(serializer.data)

class MajorInDetail(APIView):
    def get(self,request,pk):
        majorin=MajorIn.object.get(pk=pk)
        serializer=MajorInSerializer(majorin)
        return response.Response(serializer.data)

    def put(self,request,pk):
        majorin=MajorIn.objects.get(pk=pk)
        serializer=MajorInSerializer(majorin,data=request.data)
        serializer.save()
        response.Response(serializer.data)

    def delete(self,request,pk):
        majorin = MajorIn.objects.get(pk=pk)
        majorin.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)



'''Enrollment'''

class EnrollmentList(APIView):
    def post(self,request):
        serializer=EnrollmentSerializer(data=request.data)
        serializer.save()
        response(serializer.data,status=status.HTTP_201_CREATED)

    def get(self,request):
        queryset=Enrollment.objects.all()
        serializer=EnrollmentSerializer(queryset,many=True)
        response.Response(serializer.data)

class EnrollmentDetail(APIView):
    def get(self,request,pk):
        enrollment=Enrollment.object.get(pk=pk)
        serializer=EnrollmentSerializer(enrollment)
        return response.Response(serializer.data)

    def put(self,request,pk):
        enrollment=Enrollment.objects.get(pk=pk)
        serializer=EnrollmentSerializer(enrollment,data=request.data)
        serializer.save()
        response.Response(serializer.data)

    def delete(self,request,pk):
        enrollment = Enrollment.objects.get(pk=pk)
        enrollment.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)







