# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from main_app.model.Treasure import Treasure
# Create your views here.

def index(request):

    return render(request, 'index.html', {'treasures':treasures})

treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM"),
    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO"),
    Treasure('Coffee Can', 20.00, 'tin', "Acme, CA")
]