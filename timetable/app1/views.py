from django.shortcuts import render

# Create your views here.
def starting_page(request):
  return render(request , "app1/main.html")
def home_page(request):
  return render(request , "app1/home.html")

