from django.urls import path
from app import views

urlpatterns = [
  path('tables/', views.TableListView.as_view()),
  path('departments/', views.DepartmentListView.as_view()),
  path('categories/', views.MealCategoryListView.as_view()),
  path('statuses/', views.StatusListView.as_view()),
  path('percentage/', views.ServicePercentageListView.as_view()),
  path('meals/', views.MealListView.as_view()),
  path('meals/<int:pk>/', views.MealDetailView.as_view()),
  path('orders/', views.OrderListView.as_view()),
  path('checks/', views.CheckListView.as_view()),
  path('checks/<int:pk>', views.CheckDetailView.as_view()),
  path('mealstoorder/', views.MealsToOrderListView.as_view()),
  path('activeorders/', views.ActiveOrderListView.as_view()),    
]

    