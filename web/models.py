import datetime
from index import db


class Release(db.Model):

    __tablename__ = 'releases'

    id = db.Column(db.String, primary_key=True)
    artist_id = db.Column(db.String, nullable=False)
    label_id = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    artist_name = db.Column(db.String, nullable=False)
    label_name = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    youtube_playlist_id = db.Column(db.String, nullable=False)
    tags = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)

    def __init__(self, title):
        self.title = title
        self.date_posted = datetime.datetime.now()
