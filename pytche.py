# -*- encoding: utf-8 -*-

# ### Pytche Site ###
#
# ### ### ### ### ###
from flask import Flask, render_template
from flask import Flask
from flask_flatpages import FlatPages
from forms import EventForm

import datetime
import simplejson

app = Flask(__name__)
app.config.from_pyfile('mysettings.cfg')
pages = FlatPages(app)

@app.route('/page/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    template = page.meta.get('template', 'flatpages.html')
    return render_template(template, page=page)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/agenda/')
def agenda():
	form = EventForm()
	return render_template('agenda.html', form=form)

@app.route('/event/<eventid>/')
def hello(eventid):
	return "Oi!" + eventid

@app.route('/events.json')
def events_json():
	today = datetime.date.today()
	events = [
				{
					'title': 'Evento HOJE o dia todo',
					'start': today.ctime(),
					'allDay': True,
					'url':'/event/5/'
				},
				{
					'title': 'Grande evento',
					'start': datetime.date(today.year, today.month, today.day-5).ctime(),
					'end': datetime.date(today.year, today.month, today.day-2).ctime(),
					'url':'/event/6/'
				}
			]
	return simplejson.dumps(events)

if __name__=="__main__":
	app.run(debug=True,port=8000)
