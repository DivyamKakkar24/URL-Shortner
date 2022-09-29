from django.shortcuts import render, HttpResponse, redirect
import uuid
from shorturl.models import Url

# Create your views here.

def index(request):
	return render(request, "index.html")


def create(request):
	if request.method == 'POST':
		link = request.POST['link']
		uid = str(uuid.uuid4())[:5]

		new_url = Url(link = link, uuid = uid)
		new_url.save()

		return HttpResponse(uid)

def go(request, s):
	original_link = Url.objects.get(uuid = s)
	return redirect(original_link.link)


