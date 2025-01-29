from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from .models import Lots, CutOfBanana
from .forms import LotForm, CutForm

    
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
            
            lots = Lots.objects.filter(local__icontains=search)
        else:

            # definir variavel com todos os objetos
            lots = Lots.objects.all()
        
        return render(request, 'partials/list-lots.html', {'lots':lots, 'form': form})

def deleteLot(request, id):
    lot = get_object_or_404(Lots, pk=id)
    cuts = CutOfBanana.objects.filter(id_lot=id)
    cuts.delete()
    lot.delete()
    messages.info(request, 'Lote deletado com sucesso!')
    return redirect('/')

def deleteCut(request, id):
    lot = get_object_or_404(Lots, pk=id)
    cuts = CutOfBanana.objects.filter(id_lot=id)
    cuts.delete()
    lot.delete()
    messages.info(request, 'Lote deletado com sucesso!')
    return redirect('/')

def viewLot(request, id):
    
    if request.method == 'POST':
        print('tem POST')
        form = CutForm(request.POST)
        if form.is_valid():
            cutLot = form.save(commit=False)
            cutLot.id_lot = int(id)
            primeira = form.cleaned_data['primeira']
            segunda = form.cleaned_data['segunda']
            kg = form.cleaned_data['kg_caixa']
            cotacao = form.cleaned_data['cotacao']
            caixas_primeira_ajust = float(kg*primeira/22)
            caixas_segunda_ajust = float(kg*segunda/22)
            cutLot.porcentagem = round(100*float(primeira/(primeira+segunda)))
            cutLot.preco = round(float(caixas_primeira_ajust*cotacao+caixas_segunda_ajust*cotacao/2))
            cutLot.save()
            return redirect('/lot/'+str(id))
        else: 
            form = CutForm()
            return render(request, 'partials/lot.html', {'form': form})
    else:
        form = CutForm()
        
        search = request.GET.get('search')
        
        if search:
            cuts = CutOfBanana.objects.filter(id_lot=id,date__icontains=search)
        else:
            cuts = CutOfBanana.objects.filter(id_lot=id).order_by('-date')
    
        lot_current = get_object_or_404(Lots, pk=id)
        
        return render(request, 'partials/lot.html', {'lot': lot_current, 'cuts': cuts, 'form': form})

def dashboard(request):
    return render(request, 'partials/dashboard.html')

