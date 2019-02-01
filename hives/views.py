from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

import datetime

from .models import Hive, Breed

def menu(request):
    context = { 'title': 'Hives' }
    return render(request, 'hives/menu.html', context)


def add(request):
    if ( request.method=='GET'):
        hive = Hive()
        queen_year = datetime.datetime.now().year
        queen_breed = ''
        status_msg = '* <small>- Indicates Required Fields</small>'
    else:
        hive = Hive()
        hive.date_entered = datetime.datetime.now()
        hive.label = request.POST['hive_label']
        hive.hive_from = request.POST['hive_from']
        hive.queen_year = int(request.POST['queen_year'])

        name = request.POST['queen_breed']
        print('looking up %s' % name)
        breeds = Breed.objects.all()
        print()
        print(breeds)
        print()
        print(name)
        print()
        queen_breed = ''
        # queen_breed = breeds.objects.all()
        for breed in breeds:
            print('%s - %s' % (breed, breed.name))
            if breed.name == name:
                print('setting breed to %s' % breed.name)
                queen_breed = breed
        print('queen_breed set to %s' % queen_breed)

        hive.queen_breed = queen_breed
        hive.queen_from = request.POST['queen_from']
        hive.location = request.POST['location']
        hive.brood_boxes = request.POST['brood_boxes']
        hive.supers = request.POST['supers']
        status_msg = 'hive "%s" has been added' % hive.label
        hive.save()
        hive = Hive()
        queen_year = hive.queen_year
        queen_breed = ''

    print('queen_year = %i' % queen_year)
    year_color = "year%i" % (queen_year % 5)
    ylst = []
    for year in range(queen_year - 10, queen_year + 3):
        ylst.append(year)
    breeds = Breed.objects.all().order_by('name')
    blst = []
    for breed in breeds:
        blst.append( breed.name)

    context = { 'title': 'Hives - Add',
                'years': ylst,
                'queen_year' : queen_year,
                'queen_breed': queen_breed,
                'year_color': year_color,
                'breeds': blst,
                'hive': hive,
                'status_msg': status_msg }
    return render(request, 'hives/add.html', context)


def build_hive_list():
    hives = Hive.objects.all().order_by('label')
    hive_list = []
    for hive in hives:
        items = {}
        items['date_entered'] = hive.date_entered
        items['label'] = hive.label
        items['hive_from'] = hive.hive_from
        items['queen_year'] = hive.queen_year
        items['queen_breed_name'] = hive.queen_breed_name()
        items['queen_color_class'] = hive.queen_color_class()
        items['queen_from'] = hive.queen_from
        items['location'] = hive.location
        items['brood_boxes'] = hive.brood_boxes
        items['supers'] = hive.supers
        hive_list.append( items)
    return hive_list

def list(request):
    hive_list = build_hive_list()
    context = { 'hive_list': hive_list }
    return render(request, 'hives/list.html', context)


def edit(request):
    hive_label = request.GET['label']
    # print('Edit %s' % hive_label)
    hive_list = build_hive_list()
    context = { 'hive_list': hive_list }
    context = { 'hive_label': hive_label}
    return render(request, 'hives/edit.html', context)


def delete(request):
    hive_label = request.GET['label']
    hive = Hive.objects.filter(label=hive_label)
    print(hive)
    hive.delete()
    print('Deleted hive "%s"' % hive_label)
    hive_list = build_hive_list()
    context = { 'hive_list': hive_list }
    context['message'] = 'hive "%s" has been deleted' % hive_label
    return render(request, 'hives/list.html', context)





# ###############################################
#
#    APIs
#
# ###############################################


# ###############################################
#
#    get_hive_simple_list
#
#    return a list of the label and location
#    of each of the hives
#
# ###############################################

def get_hive_simple_list(request):
    hives = Hive.objects.all().order_by('label')
    jason_data = []
    for hive in hives:
        items = {}
        items['label'] = hive.label
        items['location'] = hive.location
        jason_data.append( items)
    return JsonResponse(jason_data, safe=False)


# ###############################################
#
#    get_hive_full_list
#
#    return a list of everything about
#    each of the hives
#
# ###############################################

def get_hive_full_list(request):
    hives = Hive.objects.all().order_by('label')
    jason_data = []
    for hive in hives:
        items = {}
        items['date_entered'] = hive.date_entered
        items['label'] = hive.label
        items['hive_from'] = hive.hive_from
        items['queen_year'] = hive.queen_year
        items['queen_breed'] = hive.queen_breed.name
        items['queen_from'] = hive.queen_from
        items['location'] = hive.location
        items['brood_boxes'] = hive.brood_boxes
        items['supers'] = hive.supers
        jason_data.append( items)
    return JsonResponse(jason_data, safe=False)


# ###############################################
#
#    is_hive_label_unique
#
#    return a list of everything about
#    each of the hives
#
# ###############################################

def is_hive_label_unique(request):
    hives = Hive.objects.all()
    target = request.GET['label']
    unique = True
    for hive in hives:
        if hive.label == target:
            unique = False
    jason_data = [{'unique': unique}]
    return JsonResponse(jason_data, safe=False)
