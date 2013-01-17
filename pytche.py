# -*- encoding: utf-8 -*-

# ### Pytche Site ###
#
# ### ### ### ### ###
from flask import Flask, render_template
from forms import EventForm
import datetime
import simplejson

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/agenda/')
def agenda():
	form = EventForm()
	return render_template('agenda.html', form=form)

@app.route('/events.json')
def events_json():
	today = datetime.date.today()
	events = [
				{
					'title': 'Evento HOJE o dia todo',
					'start': today.ctime(),
					'allDay': True,
					'url':'http://pytche.org/event/5'
				},
				{
					'title': 'Grande evento',
					'start': datetime.date(today.year, today.month, today.day-5).ctime(),
					'end': datetime.date(today.year, today.month, today.day-2).ctime(),
					'url':'http://pytche.org/event/6'
				}
			]
	return simplejson.dumps(events)

if __name__=="__main__":
	app.run(debug=True)
