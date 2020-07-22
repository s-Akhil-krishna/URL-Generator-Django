from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from shortener.models import KirrURL
from .forms import SubmitUrlForm
from analytics.models import ClickEvent


class HomeView(View):
	def get(self,request,*args,**kwargs):
		form = SubmitUrlForm()
		context = {
			'title':'SubmitURL',
			'form':form
		}
		return render(request,'shortener/home.html',context)

	def post(self,request,*args,**kwargs):
		form = SubmitUrlForm(request.POST)
		template = 'shortener/home.html'
		if form.is_valid():
			print(form.cleaned_data)
			new_url = form.cleaned_data.get('url')
			obj , created = KirrURL.objects.get_or_create(url=new_url)

			context = {
				'created':created,
				'title':'SubmitURL',
				'form': form,
				'object':obj

			}

			if created:
				template = 'shortener/success.html'
			else:
				template = 'shortener/exists.html'
		
		return render(request,template,context)


class URLRedirectview(View):
	def get(self,request,shortcode=None,*args,**kwargs):
		obj = get_object_or_404(KirrURL,shortcode=shortcode)		
		count = ClickEvent.objects.create_event(obj)
		print(count)
		return HttpResponseRedirect(obj.url)








