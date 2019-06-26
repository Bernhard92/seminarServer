<form id="form" action="/check_test" method="post">
	{% csrf_token %}
	<div class="names">
		<div class="form-group">
				<label for="usr">Vorname:</label>
				<input type="text" class="form-control" name="firstname" id="usr">
		</div>
		<div class="form-group">
				<label for="usr">Nachname:</label>
				<input type="text" class="form-control" name="lastname" id="usr">
		</div>
	</div>
	{% for key, value in questions.items %}			
		<div id=questions>
		<p>{{ key }}</p>
		
			{% for answer in value %}
				<div class="form-check">
					<label class="form-check-label"><input type="radio" name="question{{ forloop.parentloop.counter }}" class="form-check-input" value="q{{ forloop.parentloop.counter }}a{{ forloop.counter }}">{{ answer }}</label>
				</div>
			{% endfor %}
		</div>
		{% endfor %} 

	<input type="submit" class="btn btn-danger" value="Fertig!">
</form>