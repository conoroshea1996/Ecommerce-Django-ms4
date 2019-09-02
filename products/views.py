from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Product, Catagory
from comments.models import Comment
from comments.forms import Message
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.


def all_products(request, catagory_name=None):
    products = Product.objects.all()
    catagorys = Catagory.objects.all()
    selected_categories = None

    if catagory_name:
        catagory = get_object_or_404(Catagory, type=catagory_name)
        products = Product.objects.filter(catagory=catagory)

    if request.GET.getlist('catagory'):
        selected_categories = Catagory.objects.filter(
            type__in=request.GET.getlist('catagory'))
       # filter products for selected categories
        products = [
            product for product in products if product.catagory in selected_categories]
        print(products)
        print(selected_categories)

    if request.is_ajax():
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        products = paginator.get_page(page)
        html = render_to_string('products.html', {'products': products})
        return HttpResponse(html)

    paginator = Paginator(products, 3)

    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'products.html', {"products": products})


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    comments = Comment.objects.filter(product__in=product_id)
    avg_rating = 0
    for rating in comments:
        avg_rating += rating.rating

    product.views += 1
    product.save()
    product_img = product.photo_set.all()

    if request.method == "POST":
        message_form = Message(request.POST)

        if message_form.is_valid():
            user_message = message_form.save(commit=False)
            user_message.save()
            return redirect(reverse('product', kwargs={'product_id': product_id}))

    return render(request, 'product.html', {"product": product, 'images': product_img, 'comment': comments, 'comment_form': Message, 'rating': avg_rating})
