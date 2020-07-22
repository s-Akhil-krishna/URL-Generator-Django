from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
 	#anything starting with www goes into the path below 
    host(r'www', settings.ROOT_URLCONF, name='www'),
    
    #any path starting with other than www goes into below path.
    host(r'(?!www).*', 'kirr.hostsconf.urls', name='wildcard'),
)