from django.shortcuts import render
from django.db.models import F

from cacke.forms import SearchForm
from .models import Bulka

# Create your views here.
def cacke_list (request):
    cackes = Bulka.objects.all()
    form = SearchForm()
    if request.method == "POST":
        form = SearchForm(request.POST) 
        
        stringe = form.get_nach()
        cackes = Bulka.objects.filter(nachinka__icontains = stringe)
        
    else:
        cackes = Bulka.objects.all()        
    return render(request, 'cacke/cacke_list.html', {'cacke':cackes,'form': form})