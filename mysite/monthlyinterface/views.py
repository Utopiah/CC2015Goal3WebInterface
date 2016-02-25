from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from .models import Creation

def index(request):
    latest_creation_list = Creation.objects.order_by('-pub_date')[:5]
    template = loader.get_template('monthlyinterface/index.html')
    context = {
        'latest_creation_list': latest_creation_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, creation_id):
    result = Creation.objects.get(pk=creation_id).details()
    template = loader.get_template('monthlyinterface/details.html')
    context = {
        'creation_id': creation_id,
        'themes': result['themes'],
        'image': result['image']
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("(UI exploration https://wireframe.cc/74FKag ) You are looking at creation %s.<br>Fork it button." % creation_id)

def requestnewcreation(request):
    template = loader.get_template('monthlyinterface/requestnewcreation.html')
    context = {}
    return HttpResponse(template.render(context, request))
    

def requestednewcreation(request):
    themes = request.POST['themes'];
    newcreationid = Creation.generate(requested_themes=themes)
    return redirect('detail', newcreationid)

def fork(request, creation_id):
    newcreationid = Creation.objects.get(pk=creation_id).fork()
    return redirect('detail', newcreationid)

