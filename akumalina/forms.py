from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class RecordingParamsForm(FlaskForm):
	duration = IntegerField('Duration', render_kw={
		'placeholder': 'Duration (s)',
		'class': 'form-control'
	})
	channel_number = IntegerField('Channel number', render_kw={
		'placeholder': 'Channel number',
		'class': 'form-control'
	})
