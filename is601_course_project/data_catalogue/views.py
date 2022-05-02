from django.http import HttpResponse
from django.shortcuts import render

from .models import DataSetDesc, DataSetDescForm, Order, Trade

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.urls import reverse

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DataSetDescSerializer


def dataview(request): 
    if request.method == 'POST':
        form = DataSetDescForm(request.POST)
        if form.is_valid():
            dataset_desc = DataSetDesc.objects.filter(**form.cleaned_data)
            context = {'dataset_desc': dataset_desc}
            return render(request, 'data_catalogue/datasets.html', context)
    else:
        form = DataSetDescForm()

    return render(request, 'data_catalogue/dataview.html', {'form': form})  

#def index(request):
#    return render(request, 'data_catalogue/index.html')


def datasets(request):
    dataset_desc = DataSetDesc.objects.all()
    context = {'dataset_desc': dataset_desc}
    return render(request, 'data_catalogue/datasets.html', context)   

def ajax(request):
    return render(request, 'data_catalogue/ajax.html')

def ajax_demo(request):
    #get as list as queryset not json serializable
    dataset_list = list(DataSetDesc.objects.values())
    
    return JsonResponse({'data' : dataset_list})  

class Home(TemplateView):
    template_name = 'data_catalogue/index.html'

class DataSetDescViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows baked goods to be viewed or edited.
    """
    queryset = DataSetDesc.objects.all()
    serializer_class = DataSetDescSerializer
    permission_classes = [permissions.IsAuthenticated]    

def tabview(request, name, env):
    if(name == 'TRADE'):
        trades = Trade.objects.filter(environment_type=env)
        tradecontext = {'trades': trades}
        return render(request, 'data_catalogue/trades.html', tradecontext)
    else:
        orders = Order.objects.filter(environment_type=env)
        ordercontext = {'orders': orders}
        return render(request, 'data_catalogue/orders.html', ordercontext)
          