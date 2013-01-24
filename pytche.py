# -*- encoding: utf-8 -*-

# ### Pytche Site ###
#
# ### ### ### ### ###
from flask import Flask, render_template, request, flash, url_for, redirect, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask_flatpages import FlatPages
from wtforms import Form, validators, DateTimeField, TextField, TextAreaField
import datetime
import simplejson

app = Flask(__name__)
try:
	app.config.from_pyfile('configuration.py')
except:
	pass
pages = FlatPages(app)
db    = SQLAlchemy(app)

class EventForm(Form):
	title = TextField( u'Título', [validators.Length(min=4, max=25)] )
	obs = TextAreaField( u'Observações', [validators.Length(min=0, max=1000)] )
	data_ini = DateTimeField( u'Data/Hora Incício', format='%d/%m/%Y %H:%M')
	data_fim = DateTimeField( u'Data/Hora Fim', format='%d/%m/%Y %H:%M')

class EventModel(db.Model):
	__tablename__ = 'evento'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column( db.String(55))
	obs = db.Column(db.Text)
	data_ini = db.Column(db.DateTime)
	data_fim = db.Column(db.DateTime)


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
	if hasattr(g,'form'):
		form = g.form
	else:
		form = EventForm()
	return render_template('agenda.html', form=form)


@app.route('/event/<eventid>/')
def hello(eventid):
	return "Oi!" + eventid


@app.route('/events/save/',methods=['POST'])
def events_save():
	form = EventForm(request.form)
	if request.method == 'POST' and form.validate():
		#try:
		evento = EventModel()
		evento.title = form['title'].data
		evento.obs = form['obs'].data
		evento.data_ini = form['data_ini'].data
		evento.data_fim = form['data_fim'].data
		db.session.add(evento)
		db.session.commit()
		flash(u"Evento salvo com sucesso.")
		# except:
		# 	flash("O Evento não pode ser criado!!")
	else:
		flash(u"Os dados informados não estão corretos.")
		g.form = form
	return redirect(url_for('agenda'))


@app.route('/events.json')
def events_json():
	today = datetime.date.today()
	evts = EventModel.objects.all()
	events = [
				{
					'title': 'Evento HOJE o dia todo',
					'start': today.ctime(),
					'allDay': True,
					'url':'/event/5'
				},
				{
					'title': 'Grande evento',
					'start': datetime.date(today.year, today.month, today.day-5).ctime(),
					'end': datetime.date(today.year, today.month, today.day-2).ctime(),
					'url':'/event/6'
				}
			]
	return simplejson.dumps(events)

if __name__=="__main__":
	app.run()
