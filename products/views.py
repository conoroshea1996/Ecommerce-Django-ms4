from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.


def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 2)  # Show 25 contacts per page

    page = request.GET.get('page')
    # contacts = paginator.get_page(page)

    try:
        product_pages = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        product_pages = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        product_pages = paginator.page(paginator.num_pages)

    if request.is_ajax():
        html = render_to_string('filter_products.html', {'products': products})
        return (html)

    return render(request, 'products.html', {"products": product_pages})


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'product.html', {"product": product})
