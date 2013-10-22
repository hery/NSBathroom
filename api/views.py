from django.http import HttpResponse

import logging
logger = logging.getLogger('nsbathroom-debug')

def index(request):
    return HttpResponse('Hello, pandas!')

def annotation(request):
	logger.debug(request.method)
	logger.debug('Received /api/annotation request.')
	title = request.GET['title']
	coordinates = request.GET['coordinates']
	response = "Received response for pin annotation entitled %s and located at %s" % (title, coordinates)
	return HttpResponse(response)