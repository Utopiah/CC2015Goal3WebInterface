from django.http import HttpResponse
from django.template import loader
import sys
sys.path.insert(0, '/home/fabien/Prototypes/CC2015Goal3Month1')

from .models import Creation

def BlendMeAPicture(string):
#import BlendMeAPicture
# problem between Python2 and Python3...
# NO, heavy processing should be done at the models side, fat models skinny views
    return "blended the images of "+string+ " topic together"
    #cheating until it (month1) becomes a library compatible to python3

def index(request):
    latest_creation_list = Creation.objects.order_by('-pub_date')[:5]
    template = loader.get_template('monthlyinterface/index.html')
    context = {
        'latest_creation_list': latest_creation_list
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse(goal  +  "<hr>" + "Expected result : " + BlendMeAPicture("no topic provided!"))

def detail(request, creation_id):
   return HttpResponse("(UI exploration https://wireframe.cc/74FKag ) You are looking at creation %s.<br>Fork it button." % creation_id)
