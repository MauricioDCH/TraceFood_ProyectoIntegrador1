from django.shortcuts import render

from pymongo import MongoClient
client = MongoClient('mongodb+srv://vguerraz:TwD374X@cluster0.ieqcc.mongodb.net/test')
db = client['TraceFood']

# Create your views here.

def recesForm(request):
    return render(request, 'recesForm.html')