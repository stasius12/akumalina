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
        pass

    @classmethod
    def create(cls, wave_file_name, time_plot_file_name=None):
        wave_file_path = self.get_default_wave_file_path(wave_file_name)
        time_plot_path = self.get_default_time_plot_path(time_plot_file_name) if time_plot_file_name else ''
        obj = cls(wave_file_path=wave_file_path, time_plot_path=time_plot_path)
        db.session.add(obj)
        db.session.commit()

    def update_time_plot_path(self, value):
        self.time_plot_path = value
        db.session.update(self)
        db.session.commit()

    @staticmethod
    def get_default_wave_file_path(file_name):
        return 'static/wave_files/%s' % file_name

    @staticmethod
    def get_default_time_plot_path(file_name):
        return 'static/time_plots/%s' % file_name
