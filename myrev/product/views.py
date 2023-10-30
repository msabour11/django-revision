from django.shortcuts import render,redirect,reverse
from product.models import Product,Category
from product.forms import ProductForm,ProductFormModel
from django.http import HttpResponse

# Create your views here.
def index(request):

    products=Product.objects.all()
    return render(request, 'product/index.html',{'products':products})




def detail(request,id):

    product=Product.objects.get(id=id)

    return render (request, 'product/detail.html',{'product':product})



def delete(request,id):
    product=Product.objects.get(id=id)
    product.delete()
    return redirect('product.index')


def create(request):
    categories=Category.objects.all()
    if request.method == 'POST':
        print(request.POST)
        title=request.POST.get('title')
        description=request.POST.get('description')
        price=request.POST.get('price')
        image=request.FILES.get('image')

        product=Product()
        product.title=title
        product.description=description
        product.price=price
        product.image=image
        product.save()
        return redirect('product.index')




    return render(request, 'product/create.html',{'categories':categories})


def create_form(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']
            price=form.cleaned_data['price']
            image=form.cleaned_data['image']
            category=form.cleaned_data['category']

            

            product=Product()
            product.title=title
            product.description=description
            product.price=price
            product.category=category
            product.image=image
            product.save()
            return redirect('product.index')
           
    

    return render(request, 'product/createform.html',{'form':form})



def create_product_Mform(request):

    form=ProductFormModel()
    if request.method == 'POST':
        form=ProductFormModel(request.POST, request.FILES)
        if form.is_valid():
            product=form.save()
            # url=reverse('product.detail', args=(product.id,))
            return redirect(product.get_detial_url())
        

    return render(request, 'product/createmodelform.html',{'form':form})


def editemodelform(request,id):
    product=Product.get_speacified_product(id=id)
    form=ProductFormModel(instance=product)
    if request.method == 'POST':
        form=ProductFormModel(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product.index')
    return render(request, 'product/edit.html', {'form':form})


# def select_category(request):
#     products=Product.objects.all()
#     products.filter(product.