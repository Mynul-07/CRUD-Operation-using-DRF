from django.shortcuts import render, get_object_or_404 # bring the data and check if it exists
#from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from rest_framework import mixins, generics, viewsets
from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializer, CommentSerializer
from .paginations import CustomPagination 


# Create your views here.
@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        # Get all the data from the Student table
        students = Student.objects.all()# fetches multiple students
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # create a new student
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT', 'DELETE'])   
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data) # update the student
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        # if the data is not valid
        return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# class Employees(APIView):
#     def get(self, request):
#         # Get all the data from the Employee table
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def post(self, request):
#         # create a new employee
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class EmployeeDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
        
        
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

"""
# Mixins
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

# Mixins for Employee Detail View   
class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
    
"""
"""
# Generic Views
class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# Generic View for Employee Detail
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'  # Allows you to use 'pk' in the URL for detail view
    
"""


"""

# viewsets.ViewSet
class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk = None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    def update(self, request, pk = None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk = None):
        employee = get_object_or_404(Employee,pk = pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
"""


# viewsets.ModelViewSet

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination  # Use custom pagination if needed
    
class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'
    
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'