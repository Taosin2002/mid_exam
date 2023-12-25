from django.shortcuts import render
from author.models import CarModel


def home(request):
    data=CarModel.objects.all()
    return render(request,'home.html',{'data':data})

