from django.shortcuts import render
from django.http import HttpResponse
from .models import Doodle
from django.template import RequestContext, loader
# Create your views here.
def index(request):
    latest_doodles = Doodle.objects.order_by('-pub_date')[:5]
    template = loader.get_template('Doodlers/index.html')
    context = RequestContext(request, {
        'latest_doodles': latest_doodles,
    })
    return render(request, 'Doodlers/index.html', context)
def doodle(request, title):
	response = "This is where %s doodle goes. Expect to see comments here" % title
def comment(request, title):
	response = "Commenting on %s doodle." % title
