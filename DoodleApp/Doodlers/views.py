from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from Doodlers.models import Doodle, Comment
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from os.path import join as pjoin
import sentiment

# Create your views here.
class IndexView(generic.ListView):
	model = Doodle
	template_name = 'Doodlers/index.html'
	context_object_name = 'latest_doodles'
	def get_queryset(self):
		return Doodle.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
def DoodleView(request, id):
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
	p = get_object_or_404(Doodle, pk=id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'Doodlers/detail.html', {
				'doodle': p,
				'error_message': "You didn't select a choice",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
 		return HttpResponseRedirect(reverse('doodle:results', args=(p.id,))) 
def upload_picture(request, id):
	p = get_object_or_404(Doodle, pk=id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'Doodlers/detail.html', {
				'doodle': p,
				'error_message': "You didn't select a choice",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
 		return HttpResponseRedirect(reverse('doodle:results', args=(p.id,))) 