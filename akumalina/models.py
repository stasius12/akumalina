from sqlalchemy.orm import validates
from akumalina import db
from datetime import datetime

class WaveFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    wave_file_path = db.Column(db.String(100))
    time_plot_path = db.Column(db.String(100))

    @validates('wave_file_path', 'time_plot_path')
    def validate_wave_file_path(self, key, path):
        raise AssertionError(key)


