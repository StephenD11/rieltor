from codecs import CodecInfo

from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import first
from .models import CompanyInfo,FAQ
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from .forms import ReviewForm
from .models import Client, Review, Property
from django.core.paginator import Paginator
from .forms import PropertySearchForm

# Create your views here.

def home(request):
    reviews = Review.objects.all().order_by('-created_at')
    paginator = Paginator(reviews, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'rieltor/home.html', {'page_obj': page_obj})


def gallery(request):
    return render(request, 'rieltor/gallery.html')


def contacts(request):
    company_info = CompanyInfo.objects.first()
    return render(request, 'rieltor/contacts.html', {'company_info': company_info})


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'rieltor/thank_you.html')
    else:
        form = ReviewForm()
    return render(request, 'rieltor/add_review.html', {'form': form})

@cache_page(60 * 15)
def property_gallery(request):
    form = PropertySearchForm(request.GET)
    properties = Property.objects.all()

    if form.is_valid():
        city = form.cleaned_data.get('city')
        price_max = form.cleaned_data.get('price_max')

        if city:
            properties = properties.filter(city__icontains=city)  # Поиск по городу
        if price_max:
            properties = properties.filter(price__lte=price_max)  # Фильтрация по максимальной цене

    paginator = Paginator(properties, 3)  # Разбиваем на страницы по 3 объекта
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'rieltor/property_gallery.html',  {'properties': page_obj, 'form': form})


def property_detail(request,pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'rieltor/property_detail.html', {'property': property})


def faq_view(request):
    faqs = FAQ.objects.all()
    return render(request, 'rieltor/faq.html', {'faqs': faqs})


