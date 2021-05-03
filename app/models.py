from django.db import models, IntegrityError
from user.models import User
from django.core.validators import MinValueValidator
from django.conf import settings


class Table(models.Model):
  name = models.CharField(max_length=100, default='')

  def __str__(self):
      return self.name

  class Meta:
    verbose_name_plural = "Tables"
  

class Department(models.Model):
  name = models.CharField(max_length=100, default='')

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = "Departments"
    

class MealCategory(models.Model):
  name = models.CharField(max_length=100, default='')
  departmentid = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department')

  def __str__(self):
      return self.name

  class Meta:
    verbose_name_plural = "MealCategories"
  

class Status(models.Model):
  name = models.CharField(max_length=100, default='')

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = "Statuses"
  

class ServicePercentage(models.Model):
  percentage = models.IntegerField(default=0)

  def __str__(self):
    return f'{str(self.percentage)}%'

  class Meta:
    verbose_name_plural = "ServicePercentages"
  

class Order(models.Model):
  waiterid = models.IntegerField(default=0)
  tableid = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='table', null=True)
  isitopen = models.BooleanField(default=0)
  date = models.DateTimeField(auto_now_add=True)

  def get_total_sum(self):
    return sum(item.get_sum() for item in self.orderid.all())

  def __str__(self):
      return str(self.waiterid)

  class Meta:
    verbose_name_plural = "Orders"
  

class Meal(models.Model):
  name = models.CharField(max_length=100, default='')
  categoryid = models.ForeignKey(MealCategory, on_delete=models.CASCADE, related_name='category')
  price = models.IntegerField(default=0)
  description = models.CharField(max_length=200, default='')

  def __str__(self):
      return self.name

  class Meta:
    verbose_name_plural = "Meals"
  

class Check(models.Model):
  waiterid = models.ForeignKey(User, on_delete=models.CASCADE)
  order = models.OneToOneField(Order, on_delete = models.CASCADE, primary_key = True, related_name='order')
  servicefee = models.ForeignKey(ServicePercentage, on_delete=models.CASCADE, related_name='servicefee')
  date = models.DateTimeField(auto_now_add=True)

  def get_total(self):
    return round((self.order.get_total_sum() * (1+(self.servicefee.percentage/100))), 2)

  def __str__(self):
      return f"Check #{self.order}"

  class Meta:
    verbose_name_plural = "Checks"
  

class MealsToOrder(models.Model):
  orderid = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='orderid')
  mealsid = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
  count = models.IntegerField(default=1)
  checkid = models.ForeignKey(Check, on_delete=models.CASCADE, related_name='checkid', null=True)

  def get_sum(self):
    return self.mealsid.price * self.count

  def __str__(self):
      return str(self.orderid)

  class Meta:
    verbose_name_plural = "MealsToOrders"