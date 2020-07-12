from django.shortcuts import render
from travello.models import Destination

# Create your views here.
def index(request):
    dests = [Destination(), Destination()]
    dests[0].desc = "Bhubaneswar is the city of temples"
    dests[0].name = "Bhubaneswar"
    dests[0].price = 160

    dests[1].desc = "Bangalore is the city of tech"
    dests[1].name = "Bangalore"
    dests[1].price = 360

    return render(request, 'index.html', {'dests': dests})