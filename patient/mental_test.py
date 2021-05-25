
from django.shortcuts import render, redirect


def isaac_test(request):
    return render(request, "Isaac Test.html")