from django.shortcuts import render, get_object_or_404


def menu(request):
    context = {}
    return render(request, 'hive_activity/menu.html', context)


def add(request):
    context = {}
    return render(request, 'hive_activity/add.html', context)


def reference(request):
    context = {}
    return render(request, 'hive_activity/reference.html', context)
