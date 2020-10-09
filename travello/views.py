from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.
def index(request):
    dest1=Destination()
    dest1.name="Mumbai"
    dest1.desc="that city never sleeps"
    dest1.img="destination_1.jpg"
    dest1.price=700
    dest1.offers=False
    
    dest2=Destination()
    dest2.name="hyderadad"
    dest2.desc="that city never sleeps"
    dest2.img="destination_2.jpg"
    dest2.price=70
    dest2.offers=True
    
    dest3=Destination()
    dest3.name="Jaipur"
    dest3.desc="that city never sleeps"
    dest3.img="destination_3.jpg"
    dest3.price=60
    dest3.offers=False
    
    dests=[dest1,dest2,dest3]
    return render(request, "index.html",{'dests':dests});