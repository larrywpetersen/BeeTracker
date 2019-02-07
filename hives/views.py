from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

import datetime

from .models import Hive, Breed, Pallet, Yard

def menu(request):
    context = { 'title': 'Hives' }
    return render(request, 'hives/menu.html', context)


def add(request):
    if ( request.method=='GET'):
        hive = Hive()
        # queen_year = datetime.datetime.now().year
        queen_breed = ''
        status_msg = ''
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
            # print('%s - %s' % (breed, breed.name))
            if breed.name == name:
                # print('setting breed to %s' % breed.name)
                queen_breed = breed
        # print('queen_breed set to %s' % queen_breed)

        hive.queen_breed = queen_breed
        hive.queen_from = request.POST['queen_from']
        # hive.pallet = request.POST['pallet']
        hive.brood_boxes = request.POST['brood_boxes']
        hive.supers = request.POST['supers']
        status_msg = 'hive "%s" has been added' % hive.label
        hive.save()
        hive = Hive()
        # queen_year = hive.queen_year
        queen_breed = ''

    # print('queen_year = %i' % queen_year)
    # queen_year = hive.queen_year
    year_color = "year%i" % (hive.queen_year % 5)
    ylst = []
    for year in range(hive.queen_year - 10, hive.queen_year + 3):
        ylst.append(year)
    breeds = Breed.objects.all().order_by('name')
    blst = []
    for breed in breeds:
        blst.append( breed.name)
    pallets = Pallet.objects.all().order_by('name')
    plst = []
    for pallet in pallets:
        plst.append(pallet.name)
        print(pallet)
        print("    %s" % pallet.name)
    print(plst)
    context = { 'title': 'Hives - Add',
                'years': ylst,
                # 'queen_year' : queen_year,
                'queen_breed': queen_breed,
                'year_color': year_color,
                'breeds': blst,
                'pallets': plst,
                'hive': hive,
                'status_msg': status_msg }
    # context['title'] = 'Add'
    context['form_action'] = '../add/'
    context['page_title'] = 'Add a Hive'
    context['submit_text'] = 'Add Hive'
    return render(request, 'hives/add_edit_hive.html', context)


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
        # items['location'] = hive.location
        items['location'] = hive.pallet.yard.name
        items['brood_boxes'] = hive.brood_boxes
        items['supers'] = hive.supers
        hive_list.append( items)
    return hive_list

def list(request):
    hive_list = build_hive_list()
    context = { 'hive_list': hive_list }
    context['title'] = 'List'
    return render(request, 'hives/list.html', context)


def edit(request):
    context = {}
    if ( request.method=='GET'):
        hive = Hive.objects.filter(label=request.GET['label'])[0]
        status_msg = ''
    else:
        hive = Hive.objects.filter(label=request.POST['hive_label'])[0]
        hive.label = request.POST['hive_label']
        hive.hive_from = request.POST['hive_from']
        hive.queen_year = int(request.POST['queen_year'])

        name = request.POST['queen_breed']
        breeds = Breed.objects.all()
        queen_breed = ''
        for breed in breeds:
            if breed.name == name:
                queen_breed = breed

        hive.queen_breed = queen_breed
        hive.queen_from = request.POST['queen_from']
        hive.pallet = request.POST['pallet']
        # print('brood boxes = %s' % request.POST['brood_boxes'])
        # print('supers = %s' % request.POST['supers'])
        hive.brood_boxes = int(request.POST['brood_boxes'])
        hive.supers = int(request.POST['supers'])
        # print('hive.brood_boxes = %i' % hive.brood_boxes)
        # print('hive.supers = %i' % hive.supers)
        status_msg = 'hive "%s" has been updated' % hive.label
        hive.save()


    year_color = "year%i" % (hive.queen_year % 5)
    ylst = []
    for year in range(hive.queen_year - 10, hive.queen_year + 3):
        ylst.append(year)
    breeds = Breed.objects.all().order_by('name')
    blst = []
    for breed in breeds:
        blst.append( breed.name)

    context = { 'title': 'Hives - Edit',
                'years': ylst,
                'year_color': year_color,
                'breeds': blst,
                'hive': hive, }

    if len(status_msg) > 0:
        context['status_msg'] = status_msg

    context['title'] = 'Edit'
    context['form_action'] = '../edit/?label=%s' % hive.label
    context['page_title'] = 'Edit Hive'
    context['hive'] = hive
    context['submit_text'] = 'Make Changes'
    return render(request, 'hives/add_edit_hive.html', context)


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
