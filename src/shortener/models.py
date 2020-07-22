from django.db import models
from .utils import create_shortcode
from django.conf import settings
from .validators import url_validator,dotcom_validator
from django_hosts.resolvers import reverse

SHORTCODE_MAX = getattr(settings,'SHORTCODE_MAX',15)


'''
Model is a db table,attributes are the fields of the model.
The url is the user url and the shortcode represents the transformed version of the same URL.
We take in a url and generate the shortcode.
'''

class KirrURLManager(models.Manager):

	def all(self,*args,**kwargs):
		qs =  super(KirrURLManager,self).all()
		qs_active = qs.filter(active=True)
		return qs_active

	#A custom method 
	#To just change all of the shortcodes at once
	#Reason: just for understnding managers. 
	def refresh_codes(self,items=None):
		new_codes =  0
		if items is not None:
			qs = self.all().order_by('-id')[:items]
			for q in qs:
				qs.shortcode = create_shortcode(q)
				q.save()
				new_codes += 1
		return f'New codes:{new_codes}'


class KirrURL(models.Model):
	url = models.CharField(max_length=120,validators=[url_validator,dotcom_validator])
	shortcode = models.CharField(max_length=SHORTCODE_MAX,unique=True,blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now = True)
	active = models.BooleanField(default=True)

	objects = KirrURLManager()

	def __str__(self):
		return self.url

	#overriding save method
	def save(self,*args,**kwargs):
		#here self is KirrURL object
		#super is the models.Model class 
		#and we call the super.save()
		if self.shortcode in (None,""):
			self.shortcode = create_shortcode(self)
		super(KirrURL,self).save(*args,**kwargs)

	def get_short_url(self):
		url_path =  reverse('scode', kwargs = {'shortcode':self.shortcode} ,host='www',scheme='http' )
		return url_path


