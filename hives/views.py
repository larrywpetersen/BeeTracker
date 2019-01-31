from django.shortcuts import render, get_object_or_404
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

def list(request):
    context = {}
    return render(request, 'hives/list.html', context)





# ###############################################
#
#    APIs
#
# ###############################################



# ###############################################
#
#    get_hive_list
#
# ###############################################

def get_hive_list(request):
    return ''