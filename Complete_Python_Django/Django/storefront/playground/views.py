from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def say_hello(request):
    # return HttpResponse('Hello World')
    # try:
        
    #     query_set = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass
    
    # product = Product.objects.filter(pk=0).first()
    queryset=Product.objects.filter(last_update__year=2021)
    
    # for product in query_set: 
    #     print(product)
    return render(request, 'hello.html',{'name':'Nabin', 'products':list(queryset)}) 