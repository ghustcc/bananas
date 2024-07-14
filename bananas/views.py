from django.shortcuts import render,get_object_or_404, redirect
from .models import Lots, CutOfBanana
from .forms import LotForm

    
def listLots(request):
    
    if request.method == 'POST':
        form = LotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = LotForm()
            return render(request, 'partials/list-lots.html', {'form': form})
    else:
        form = LotForm()

        # search system
        search = request.GET.get('search')
        
        if search:
            
            lots = Lots.objects.filter(title__icontains=search,description__icontains=search)
        else:

            # definir variavel com todos os objetos
            lots = Lots.objects.all()
        
        return render(request, 'partials/list-lots.html', {'lots':lots, 'form': form})

def dashboard(request):
    return render(request, 'partials/dashboard.html')