from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login),
    path('authenticate/', views.Authenticate),
    path('incentive/', views.Incentive),
    path('holiday/', views.Holiday)

]