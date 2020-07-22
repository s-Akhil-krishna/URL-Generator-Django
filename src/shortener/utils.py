import random,string
from django.conf import settings

SHORTCODE_MIN  = getattr(settings,'SHORTCODE_MIN',6)



def code_generator(size=SHORTCODE_MIN,chars = string.ascii_lowercase + string.digits ):
	return "".join(random.choice(chars) for _ in range(6))

def create_shortcode(instance,size=SHORTCODE_MIN):
	new_code = code_generator(size=size)
	
	#obtain the class from its instance
	Klass = instance.__class__ 
	qs = Klass.objects.filter(shortcode = new_code)
	if qs.exists():
		return create_shortcode(instance,size)

	return new_code
