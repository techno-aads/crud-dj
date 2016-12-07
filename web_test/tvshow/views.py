from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from .models import Show
# Create your views here.
def index(request):
    list_shows = Show.objects.order_by('broadcast_date')
    template = loader.get_template('index.html')
    context = RequestContext(request, {'list_shows' : list_shows,})
    return HttpResponse(template.render(context))



