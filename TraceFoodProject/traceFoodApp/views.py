from django.shortcuts import render

# Create your views here.

def recesForm(request):
    return render(request, 'recesForm.html')