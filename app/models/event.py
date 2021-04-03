from .db import db
from .attending import attending
from .detail_image import detail_image

class Event(db.Model):
  __tablename__ = 'events'

  id = db.Column(db.Integer, primary_key=True)
  onwer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  date_time = db.Column(db.Date)
  min_group = db.Column(db.Integer)
  max_group = db.Column(db.Integer)
  longitude = db.Column(db.Float)
  latitude = db.Column(db.Float)
  title = db.Column(db.String(100))
  description = db.Column(db.Text)
  closes = db.Column(db.Date)
  tags = db.Column(db.Text)

  host = db.relationship('User', back_populates='hosted_events')
  comments = db.relationship('EventPost', back_populates='event')
  attendees = db.relationship('User', secondary=attending)
  images = db.relationship('Image', secondary=detail_image)

  def to_public(self):
    return {
      'Host': self.host.to_public(),
      'AttendingUsers': [attendee.to_public() for attendee in self.attendees],
      'DetailPhotos': [image.to_public() for image in self.images],
      'longitude': self.longitude,
      'latitude': self.latitude,
      'title': self.title,
      'description': self.description,
      'closes': self.closes,
      'tags': self.tags,
      'comments': [comment.to_public() for comment in self.comments]
    }
