from django.shortcuts import render
from django.http import HttpResponse
from .models import Doodle, Comment
from django.template import RequestContext, loader
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'Doodlers/index.html'
    context_object_name = 'latest_doodles'
    def get_queryset(self):
    	return Doodle.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
class DoodleView(generic.DetailView):
	model = Doodle
	template_name = 'Doodlers/doodle.html'
	def get_queryset(self):
 		"""Don't show Doodles that haven't been published"""
 		return Doodle.objects.filter(pub_date__lte=timezone.now())
def comment(request, id):
	p = get_object_or_404(Doodle, pk=id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
				'poll': p,
				'error_message': "You didn't select a choice",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
 		return HttpResponseRedirect(reverse('polls:results', args=(p.id,))) 
def upload_picture(request, pk):
    profile = UserProfile.objects.get(user=pk)
    img = None

    if request.method == "POST":
        pf = ProfileForm(request.POST, request.FILES, instance=profile)
        if pf.is_valid():
            pf.save()
            # resize and save image under same filename
            imfn = pjoin(MEDIA_ROOT, profile.avatar.name)
            im = PImage.open(imfn)
            im.thumbnail((160,160), PImage.ANTIALIAS)
            im.save(imfn, "JPEG")
    else:
        pf = ProfileForm(instance=profile)

    if profile.avatar:
        img = "/media/" + profile.avatar.name
    return render_to_response("Doodlers/doodle.html", add_csrf(request, pf=pf, img=img))
