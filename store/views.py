from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ProductForm, ImageForm
from django.forms import inlineformset_factory

# Create your views here.
def home_view(request):
    context = {
        'products': Product.objects.all(),
        'brands': Brand.objects.all(),
        'categories': Category.objects.all(),
        'images': Image.objects.all(),
        'colors': Color.objects.all()
    }
    return render(request, 'index.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {'product': product}
    return render (request, 'product-detail.html', context)


def product_create(request):
    ImageFormSet = inlineformset_factory(Product, Image, form=ImageForm, extra=1, can_delete=False)

    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES, instance=Product())

        if product_form.is_valid() and image_formset.is_valid():
            product = product_form.save()
            images = image_formset.save(commit=False)
            for image in images:
                image.product = product
                image.save()
            return redirect('home')  
    else:
        product_form = ProductForm()
        image_formset = ImageFormSet(instance=Product())

    context = {
        'product_form': product_form,
        'image_formset': image_formset,
    }

    return render(request, 'product-create.html', context)