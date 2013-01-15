# -*- encoding: utf-8 -*-
from wtforms import Form, TextField, DateTimeField, validators

class EventForm(Form):
	title = TextField( u'Título', [validators.Length(min=4, max=25)] )
	obs = TextField( u'Observações', [validators.Length(min=0, max=1000)] )
	data_ini = DateTimeField( u'Data/Hora Incício', format='%d/%m/%Y %H:%M')
	data_fim = DateTimeField( u'Data/Hora Fim', format='%d/%m/%Y %H:%M')
