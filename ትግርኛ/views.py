from django.shortcuts import render
from .models import ልጣፍ
# Create your views here.

def tiglog(request):
    context = {}
    context["dataset"] = ልጣፍ.objects.all()
    return render(request, 'ትግርኛ/tiglog.html', context=context)