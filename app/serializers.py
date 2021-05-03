from rest_framework import serializers
from .models import *

class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table
        fields = ('name',)


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('name',)


class MealCategorySerializer(serializers.HyperlinkedModelSerializer):
    departmentid = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    class Meta:
        model = MealCategory
        fields = ('name', 'departmentid')


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ('name',)


class ServicePercentageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServicePercentage
        fields = ('percentage',)


class MealSerializer(serializers.HyperlinkedModelSerializer):
    categoryid = serializers.PrimaryKeyRelatedField(queryset=MealCategory.objects.all())

    class Meta:
        model = Meal
        fields = ('id', 'name', 'categoryid', 'price', 'description')


class MealsToOrderSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='mealsid.name', read_only=True)
    price = serializers.CharField(source='mealsid.price', read_only=True)
    total = serializers.FloatField(source='get_sum', read_only=True)

    class Meta:
        model = MealsToOrder
        fields = ('name', 'count', 'price', 'total')


class OrderSerializer(serializers.ModelSerializer):
    mealsid = MealsToOrderSerializer(many=True, required=False, source='orderid')
    tableid = serializers.PrimaryKeyRelatedField(queryset=MealCategory.objects.all())
    tablename = serializers.CharField(source='tableid.name', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'waiterid', 'tableid', 'tablename', 'isitopen', 'date', 'mealsid')


class CheckSerializer(serializers.ModelSerializer):
    orderid = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), source='order.id')
    servicefee = serializers.FloatField(source='servicefee.percentage', read_only=True)
    meals = MealsToOrderSerializer(many=True, required=False, source='checkid')
    totalsum = serializers.FloatField(source='get_total', read_only=True)

    class Meta:
        model = Check
        fields = ['orderid', 'waiterid', 'date', 'servicefee', 'totalsum', 'meals']