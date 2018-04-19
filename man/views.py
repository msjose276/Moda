from django.shortcuts import render

# Create your views here.
from django.db import models
from django.http import HttpResponse
from .models import Shirt
from .models import Pant
from .models import Jacket
from .models import T_shirt
from .models import Slides



from django.template import loader


def about(request):
    template = loader.get_template('Man/../static/snippets/snip_about.html')

    return render(request, 'Man/../static/snippets/snip_about.html')

def home(request):
    list_of_slides = Slides.objects.order_by('Title')
    template = loader.get_template('home.html')
    context = {
        'list_of_slides': list_of_slides,
    }
    return HttpResponse(template.render(context, request))
def home2(request):
    list_of_pants = Pant.objects.order_by("Price")  # [:5]
    list_of_shirts = Shirt.objects.order_by("Price")
    list_of_jackets = Jacket.objects.order_by('Price')
    list_of_t_shirts = T_shirt.objects.order_by('Price')

    list_of_all_material_available = []

    if list_of_pants:
        list_of_all_material_available.append(list_of_pants)

    if list_of_shirts:
        list_of_all_material_available.append(list_of_shirts)

    if list_of_jackets:
        list_of_all_material_available.append(list_of_jackets)

    if list_of_t_shirts:
        list_of_all_material_available.append(list_of_t_shirts)

    template = loader.get_template('Man/../static/templates/home.html')
    context = {
        'list_of_pants': list_of_pants,
        'list_of_shits': list_of_shirts,
        'list_of_jackets': list_of_jackets,
        'list_of_t_shirts': list_of_t_shirts,
        'list_of_all_material_available': list_of_all_material_available,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    # latest_pant_list = Pant.objects.order_by("Price")#[:5]
    # template = loader.get_template('Man/index.html')
    # context = {
    #      'latest_pant_list': latest_pant_list,
    # }
    # return HttpResponse(template.render(context, request))
    return render(request, 'home.html')

def man(request):
    list_of_pants = Pant.objects.order_by("Price")  # [:5]
    list_of_shirts = Shirt.objects.order_by("Price")
    list_of_jackets = Jacket.objects.order_by('Price')
    list_of_t_shirts = T_shirt.objects.order_by('Price')

    list_of_all_material_available = []

    if list_of_pants:
        list_of_all_material_available.append(list_of_pants)

    if list_of_shirts:
        list_of_all_material_available.append(list_of_shirts)

    if list_of_jackets:
        list_of_all_material_available.append(list_of_jackets)

    if list_of_t_shirts:
        list_of_all_material_available.append(list_of_t_shirts)

    template = loader.get_template('snippets/snip_man.html')
    context = {
        'list_of_pants': list_of_pants,
        'list_of_shits': list_of_shirts,
        'list_of_jackets': list_of_jackets,
        'list_of_t_shirts': list_of_t_shirts,
        'list_of_all_material_available': list_of_all_material_available,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'snippets/snip_man.html')

def about(request):
    return render(request, 'snippets/snip_about.html')

def AllMaterialAvailable(request):
    list_of_pants = Pant.objects.order_by("Price")#[:5]
    list_of_shirts = Shirt.objects.order_by("Price")
    list_of_jackets = Jacket.objects.order_by('Price')
    list_of_t_shirts = T_shirt.objects.order_by('Price')

    list_of_all_material_available = []

    if list_of_pants:
        list_of_all_material_available.append(list_of_pants)

    if list_of_shirts:
        list_of_all_material_available.append(list_of_shirts)

    if list_of_jackets:
        list_of_all_material_available.append(list_of_jackets)

    if list_of_t_shirts:
        list_of_all_material_available.append(list_of_t_shirts)

    template = loader.get_template('Man/index.html')
    context = {
        'list_of_pants': list_of_pants,
        'list_of_shits': list_of_shirts,
        'list_of_jackets': list_of_jackets,
        'list_of_t_shirts': list_of_t_shirts,
        'list_of_all_material_available': list_of_all_material_available,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def slides(request):
    list_of_slides = Slides.objects.order_by('Title')
    template = loader.get_template('snippets/snip_slides.html')
    context = {
        'list_of_slides': list_of_slides,
    }
    return HttpResponse(template.render(context, request))