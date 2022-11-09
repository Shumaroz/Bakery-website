from django.shortcuts import render
from django.db.models import F

from cacke.forms import SearchForm
from .models import Bulka

# Create your views here.
def cacke_list (request):
    cakes = Bulka.objects.all()
    form = SearchForm()
    if request.method == "POST":
         if(request.POST.get('Submit')):
            
            form = SearchForm(request.POST) 
            cakes = Bulka.objects.all()
       
            pric = form.get_price()
            if pric[0] == "":
                pric[0] = 0
            if pric[1] =="":
                pric[1] = 100000000000
            pric[1]= str(int(pric[1])+1)
            nam = form.get_name()
            test = form.get_test()
            stringe = form.get_nach()
            cakes = cakes.filter(nachinka__icontains = stringe).filter(testo__icontains = test).filter(name__icontains = nam).exclude(price__gte = pric[1]).filter(price__gte=pric[0])
            
         if(request.POST.get('Reset')):
            cakes=Bulka.objects.all()
            form = SearchForm()

 
            
          
    return render(request, 'cacke/cacke_list.html', {'cacke':cakes,'form': form})