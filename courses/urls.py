from django.urls import path
from . import views

urlpatterns = [
    path('course_list',views.course_list)
]
