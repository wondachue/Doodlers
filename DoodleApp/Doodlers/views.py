from django.shortcuts import render
from django.http import HttpResponse
from .models import Doodle, Comment
from django.template import RequestContext, loader

import sentiment

# Create your views here.
def index(request):
    latest_doodles = Doodle.objects.order_by('-pub_date')[:5]
    template = loader.get_template('Doodlers/index.html')
    context = RequestContext(request, {
        'latest_doodles': latest_doodles,
    })
    return render(request, 'Doodlers/index.html', context)
def doodle(request, id):
	response = "This is where %s doodle goes. Expect to see comments here" % Doodle.objects.get(pk=id).title
	template = loader.get_template('Doodlers/doodle.html')
	current_doodle = Doodle.objects.get(pk=id);
	comments = current_doodle.comment_set.all()
	scores = {}
	num_bad = 0
	for comment in comments:
		scores[comment.id] = sentiment.getSentiment(comment.comment_text)
		if scores[comment.id] < 0:
			num_bad += 1

	context = RequestContext(request, {
		'doodle': current_doodle.title,
		'comments': comments,
		'scores': scores,
		'num_bad': num_bad,
	})
	return render(request, 'Doodlers/doodle.html', context)
def comment(request, id):
	response = "Commenting on %s doodle." % Doodle.objects.get(pk=id)
	context = RequestContext(request, {
		'comment': Doodle.objects.get(pk=id),
	})
	return render(request, 'Doodlers/comment.html', context)