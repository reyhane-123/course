from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
list1=[
    {"name":"html and css", "teacher":"ahamadi","price":4000000},
]

def course_list(request):
    context={"course1":list1}
    return render(request,'course/in.html',context=context)
