from django.http import HttpResponse
from django.template import loader
import sys
sys.path.insert(0, '/home/fabien/Prototypes/CC2015Goal3Month1')

from .models import Creation

def index(request):
    latest_creation_list = Creation.objects.order_by('-pub_date')[:5]
    template = loader.get_template('monthlyinterface/index.html')
    context = {
        'latest_creation_list': latest_creation_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, creation_id):
    result = Creation.objects.get(pk=creation_id).generate()
    template = loader.get_template('monthlyinterface/details.html')
    context = {
        'image': result['image']
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("(UI exploration https://wireframe.cc/74FKag ) You are looking at creation %s.<br>Fork it button." % creation_id)
