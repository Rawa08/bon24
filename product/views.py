from django.shortcuts import render
from .models import Product, Brand
from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector

#test
import urllib
#test


# Create your views here.
      
brand = Brand.objects.all().order_by('name')


          


def home(request):
    active_product = Product.objects.all().filter(show=True).order_by('-score', '-brand_name')
    
    #Paginator
    paginator = Paginator(active_product, 20)
    page = request.GET.get("page")
    active_product = paginator.get_page(page)

    #Filterd by search
    searchProduct = request.GET.get("do_search")
    if searchProduct:
        active_product = Product.objects.annotate(search=SearchVector('name', 'id', 'sex','brand_name')).filter(search=searchProduct)
         
        
        


    
    return render(request, 'index.html', {'productObject': active_product})


def brandFilter(request,bName):
    active_product = Product.objects.all().filter(show=True, brand_name=bName).order_by('-score')
    
    paginator = Paginator(active_product, 20)
    page = request.GET.get("page")
    active_product = paginator.get_page(page)
    
    return render(request, 'index.html',{'productObject': active_product} )



def selectedProduct(request,id):
    active_product = Product.objects.all().filter(show=True, id=id)
    return render(request, 'product.html',{'productObject': active_product} )


def gType(request,gender):
    if gender == 'M' or 'W' or 'U':
        active_product = Product.objects.all().filter(show=True, sex=gender)
    if gender == 'P':
        active_product = Product.objects.all().filter(show=True, p_type="Standard package")
    if gender == 'O':
        active_product = Product.objects.all().filter(show=True).exclude(p_type="Standard package")         
    
    paginator = Paginator(active_product, 20)
    page = request.GET.get("page")
    active_product = paginator.get_page(page)
 
    return render(request, 'index.html',{'productObject': active_product} )                       
                                                     
def scoreAdd(request,):
    objectP = Product.objects.all().filter(p_type="Standard package")
    for p in objectP:
        p.score = p.score+1
        p.save()
        print(p.score)
    return render(request, 'index.html')                                                           
                                                   



def save_image(request):
    product = Product.objects.all().filter()
    for p in product:
        filename1 = p.image_link.replace(" ", "%20")
    
        print(filename1)
        urllib.request.urlretrieve(filename1, str(p.id)+".jpg")
        print("image retrived")
   
    