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
    creation = Creation.objects.get(pk=creation_id)
    result = creation.details()
    history = creation.history()
    template = loader.get_template('monthlyinterface/detail.html')
    context = {
        'creation_id': creation_id,
        'history': history,
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
    size = request.POST['size'];
    quantity_requested = 1;
    creations = Creation.generate(requested_themes=themes, requested_size=size, quantity=quantity_requested)
    if quantity_requested == 1:
        return redirect('detail', list(creations)[0])
        # basically losing, or rather not displaying all remaining created oned n+1, n+2, etc
        # should instead redirect if only one creation and if more display a list
    else :
        return redirect('specificlist', list(creations))
        # see http://stackoverflow.com/questions/249110/django-arbitrary-number-of-unnamed-urls-py-parameters

def fork(request, creation_id):
    newcreationid = Creation.objects.get(pk=creation_id).fork()
    return redirect('detail', newcreationid)

def specificlist(request, creation_list):
    #latest_creation_list = Creation.objects.order_by('-pub_date')[:5]
    # copied from index view
    template = loader.get_template('monthlyinterface/specificlist.html')
    context = {
        'creation_list': creation_list
    }
    return HttpResponse(template.render(context, request))

