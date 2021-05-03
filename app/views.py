from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions

from .models import *
from .serializers import *

# Table
class TableListView(generics.ListAPIView):
  serializer_class = TableSerializer
  queryset = Table.objects.all()

  def get(self, request):
    tables = Table.objects.all()
    serializer = TableSerializer(tables, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request):
    serializer = TableSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


class TableDetailView(APIView):
  def get_object(self, pk):
    return Table.objects.get(pk=pk)

  def get(self, request, pk):
    tables = self.get_object(pk)
    serializers = TableSerializer(tables)
    return Response(serializers.data)

  def delete(self, request, pk, format=None):
    serializer = self.get_object(pk)
    serializer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



#Department
class DepartmentListView(generics.ListAPIView):
  serializer_class = DepartmentSerializer
  queryset = Department.objects.all()

  def get(self, request):
    department = Department.objects.all()
    serializer = DepartmentSerializer(department, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


class DepartmentDetailView(APIView):
  def get_object(self, pk):
    return Department.objects.get(pk=pk)

  def get(self, request, pk):
    departments = self.get_object(pk)
    serializers = MealSerializer(departments)
    return Response(serializers.data)

  def delete(self, request, pk, format=None):
    serializer = self.get_object(pk)
    serializer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



#Meal Category
class MealCategoryListView(generics.ListAPIView):
  serializer_class = MealCategorySerializer
  queryset = MealCategory.objects.all()
  search_fields = ['departmentid__name', ]

  def get(self, request):
    roles = MealCategory.objects.all()
    serializer = MealCategorySerializer(roles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request):
    serializer = MealCategorySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


class MealCategoryDetailView(APIView):
  def get_object(self, pk):
    return MealCategory.objects.get(pk=pk)

  def get(self, request, pk):
    mealcategory = self.get_object(pk)
    serializers = MealCategorySerializer(mealcategory)
    return Response(serializers.data)

  def delete(self, request, pk, format=None):
    serializer = self.get_object(pk)
    serializer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



# Status
class StatusListView(generics.ListAPIView):
  serializer_class = StatusSerializer
  queryset = Status.objects.all()

  def get(self, request):
    roles = Status.objects.all()
    serializer = StatusSerializer(roles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request):
    serializer = StatusSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


class StatusDetailView(APIView):
  def get_object(self, pk):
    return Status.objects.get(pk=pk)

  def get(self, request, pk):
    statuses = self.get_object(pk)
    serializers = StatusSerializer(statuses)
    return Response(serializers.data)

  def delete(self, request, pk, format=None):
    serializer = self.get_object(pk)
    serializer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



# ServicePercentage
class ServicePercentageListView(generics.ListAPIView):
  serializer_class = ServicePercentageSerializer
  queryset = ServicePercentage.objects.all()

  def get(self, request):
    roles = ServicePercentage.objects.all()
    serializer = ServicePercentageSerializer(roles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request):
    serializer =  ServicePercentageSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


class ServicePercentageDetailView(APIView):
  def get_object(self, pk):
    return ServicePercentage.objects.get(pk=pk)

  def get(self, request, pk):
    percentages = self.get_object(pk)
    serializers = ServicePercentageSerializer(percentages)
    return Response(serializers.data)

  def delete(self, request, pk, format=None):
    serializer = self.get_object(pk)
    serializer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



# Meal
class MealListView(generics.ListAPIView):
  serializer_class = MealSerializer
  queryset = Meal.objects.all()

  def get(self, request):
    serializer = MealSerializer(Meal.objects.all(), many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = MealSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealDetailView(APIView):
  def get_object(self, pk):
    return Meal.objects.get(pk=pk)

  def get(self, request, pk):
    meals = self.get_object(pk)
    serializers = MealSerializer(meals)
    return Response(serializers.data)

  def delete(self, request, pk, format=None):
    serializer = self.get_object(pk)
    serializer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



# Order
class OrderListView(generics.ListAPIView):
  serializer_class = OrderSerializer
  queryset = Order.objects.all()

  def get(self, request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(APIView):
  def get_object(self, pk):
    return Order.objects.get(pk=pk)

  def get(self, request, pk):
    orders = self.get_object(pk)
    serializers = OrderSerializer(orders)
    return Response(serializers.data)

  def delete(self, request, pk, format=None):
    serializer = self.get_object(pk)
    serializer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



# Active Orders
class ActiveOrderListView(APIView):
  def get(self, request):
    orders = Order.objects.filter(isitopen=1)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)



# Checks
class CheckListView(generics.ListAPIView):
  serializer_class = CheckSerializer
  queryset = Check.objects.all()

  def get(self, request):
    checks = Check.objects.all()
    serializer = CheckSerializer(checks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request):
    serializer = CheckSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckDetailView(APIView):
  def get_object(self, pk):
    return Check.objects.get(pk=pk)

  def get(self, request, pk):
    checks = self.get_object(pk)
    serializers = MealSerializer(checks)
    return Response(serializers.data)

  def delete(self, request, pk, format=None):
    serializer = self.get_object(pk)
    serializer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Meal To Order
class MealsToOrderListView(generics.ListAPIView):
  serializer_class = MealsToOrderSerializer
  queryset = MealsToOrder.objects.all()

  def get(self, request):
    mealstoorder = MealsToOrder.objects.all()
    serializer = MealsToOrderSerializer(mealstoorder, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request):
    serializer = MealsToOrderSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)