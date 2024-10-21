from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem

def say_hello(request):
    # return HttpResponse('Hello World')
    # try:
        
    #     query_set = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass
    
    # product = Product.objects.filter(pk=0).first()
    # queryset=Product.objects.filter(last_update__year=2021)
    
    # Product: inventory < 10 AND price <20
    # queryset=Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    
    # Product: inventory < 10 OR price <20
    # queryset=Product.objects.order_by('unit_price' ,'-title')
    
    # Limiting Results
    # queryset = Product.objects.all()[5:10]
    
    # Selecting fields to query
    # queryset = Product.objects.values_list('id', 'title', 'collection__title')
    
    # Select a product that have been ordered and sort them by title.
    # queryset = Product.objects.filter(
    #     id__in=OrderItem.objects.values('product__id').distinct()).order_by('title')
    
    # selecting related objects
    # queryset = Product.objects.select_related('collection__someOtherField').all()
    queryset = Product.objects.prefetch_related('promotions').all()
    
    # for product in query_set: 
    #     print(product)
    return render(request, 'hello.html',{'name':'Nabin', 'products':list(queryset)}) 