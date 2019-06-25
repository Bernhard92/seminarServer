from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('end_test/index.html')

    

    questions = {
    	'This is question 2': ['answer 1', 'answer 2', 'answer 3', 'answer 4'],
    	'This is question 3': ['answer 1', 'answer 2', 'answer 3', 'answer 4'],
    	'This is question 1': ['answer 1', 'answer 2', 'answer 3', 'answer 4'],
    	'This is question 4': ['answer 1', 'answer 2', 'answer 3', 'answer 4'],
    	'This is question 5': ['answer 1', 'answer 2', 'answer 3', 'answer 4'],
    	'This is question 6': ['answer 1', 'answer 2', 'answer 3', 'answer 4'],
    }

    context = {
        'questions': questions
    }
    return HttpResponse(template.render(context, request))

def check_test(request):
	return HttpResponse('hallo')