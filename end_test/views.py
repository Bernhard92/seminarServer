from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from end_test.models import TestParticipant

_NUMBER_OF_ANSWERS = 3
_NUMBER_OF_QUESTIONS = 10
_CORRECT_ANSWERS = ['q1a2','q2a2','q3a2','q4a1','q5a1','q6a3','q7a3','q8a2','q9a2','q10a1']
_QUESTIONS = {
    	'1.	Was ist <b> keine </b> Cannabinoid-Art?': ['Endocannabinoide', 'Plasmacannabinoide', 'Phytocannabinoide'],
    	'2.	THC und CBD: Welche Aussage stimmt <b>nicht</b>?': ['THC hat viele gesundheitlich vorteilhafte Wirkungen.', 'CBD und THC sind beide frei verkäuflich.', 'CBD hat keine Rauschwirkung.'],
    	'3.	Unter welcher Produktbezeichnung darf CBD <b>nicht</b> verkauft werden? ': ['Aromaprodukt ', 'Nahrungsmittelzusatz', 'Tabakersatz'],
    	'4.	Bei welchen Beschwerden kann CBD helfen? ': ['Parkinson', 'Lähmungserscheinungen ', 'Leukämie'],
    	'5.	Was bedeutet AC-zertifiziert? ': ['Gütesiegel für CBD-Produkte', 'Staatliches Siegel für CBD-Produkte', 'Gütesiegel für Regionalität'],
    	'6.	Wie viel Prozent CBD sind in Kristallen enthalten? ': ['78,9%', '89,9%', '98,9%'],
    	'7.	Was bedeutet CBD Vollextrakt ': ['Im Produkt ist nur der Wirkstoff CBD enthalten.', 'Das Produkt ist in Kristallform mit sehr hohem CBD-Anteil.', 'Im Produkt sind alle Wirkstoffe der Pflanze enthalten.'],
    	'8.	Welches CBD-Öl Pur bieten wir nicht an? ': ['5%', '15%', '25%'],
    	'9.	Welche Geschmacksrichtung bieten wir <b>nicht</b> an?': ['Ananas', 'Mango', 'Zitrone'],
    	'10. Welche weiteren Produkte bieten wir an bzw. sind in Planung? ': ['Veterinärmedizin', 'Kleidung ', 'Rohstoffmaterial '],
    }


def index(request):
    template = loader.get_template('end_test/index.html')
    context = {
        'questions': _QUESTIONS
    }

    return HttpResponse(template.render(context, request))


def check_test(request):
	if request.method =='POST':
		form = request.POST
		firstname = form['firstname']
		lastname = form['lastname']
		test_date = timezone.now()
		answers = []
		questions = _QUESTIONS

		correct_or_incorrect = []
		correct_answers = 0
		for i in range(_NUMBER_OF_QUESTIONS):
			if 'question'+str(i+1) in form:
				given_answer = form['question'+str(i+1)]
				answers.append(given_answer)
				if(given_answer in _CORRECT_ANSWERS):
					correct_answers += 1
					correct_or_incorrect.append(correct_answer_colors(i))
				else:
					correct_or_incorrect.append(false_answer_colors(i, given_answer))
			else:
				correct_or_incorrect.append(false_answer_colors(i, '0'))


				
		print(firstname)
		print(lastname)
		print(test_date)
		print('ANSWERS:', answers)
		print(correct_answers/len(_CORRECT_ANSWERS))

		answers_to_store = TestParticipant(firstname=firstname, lastname=lastname, 
			test_date=test_date, answers=answers, result=correct_answers/len(_CORRECT_ANSWERS))


		#answers_to_store.save()

		template = loader.get_template('end_test/results.html')
		context = {
			'questions': _QUESTIONS,
			'results': correct_or_incorrect,
			'answers': _CORRECT_ANSWERS,
		}

	return HttpResponse(template.render(context, request))

def correct_answer_colors(question_id):
	correct_answer = _CORRECT_ANSWERS[question_id]
	correct_postion = int(correct_answer[-1:])
	
	background_colors = []
	for i in range(1,_NUMBER_OF_ANSWERS+1):
		if(i == correct_postion):
			background_colors.append('green')
		else:
			background_colors.append('none')

	return background_colors

def false_answer_colors(question_id, given_answer):
	given_answer_position = int(given_answer[-1:])

	correct_answer = _CORRECT_ANSWERS[question_id]
	correct_postion = int(correct_answer[-1:])
	
	background_colors = []
	for i in range(1,_NUMBER_OF_ANSWERS+1):
		if(i == correct_postion):
			background_colors.append('green')
		elif(i == given_answer_position):
			background_colors.append('red')
		else:
			background_colors.append('none')

	return background_colors

