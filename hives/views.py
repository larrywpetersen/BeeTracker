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
        status_msg = '* <small>- Indicates Required Fields</small>'
    else:
        hive = Hive()
        # hive.date_entered = timezone.now().strftime( '%Y-%m-%d')
        hive.label = request.POST['hive_label']
        hive.hive_from = request.POST['hive_from']
        hive.queen_year = request.POST['queen_year']

        name = request.POST['queen_breed']
        print('looking up %s' % name)
        breeds = Breed.objects.all()
        print()
        print(breeds)
        print()
        this_breed = breeds.objects.all()
        for breed in breeds:
            print(breed)
            if breed.name == name:
                this_breed = breed.id

        hive.queen_breed = this_breed
        hive.queen_from = request.POST['queen_from']
        hive.location = request.POST['location']
        hive.brood_boxes = request.POST['brood_boxes']
        hive.supers = request.POST['supers']
        hive.save()
        queen_year = hive.queen_year.year
        status_msg = '* <small>- Indicates Required Fields</small>'

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
                'year_color': year_color,
                'breeds': blst,
                'hive': hive, }
    return render(request, 'hives/add.html', context)


def do_add(request):
    context = {}
    return render(request, 'hives/add.html', context)


