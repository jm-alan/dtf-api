from .db import db

class Image(db.Model):
  __tablename__ = 'images'

  id = db.Column(db.Integer, primary_key=True)
  url = db.Column(db.Text)

  users = db.relationship('User', back_populates='avatar')
  events = db.relationship('Event', secondary=detail_images)

  def to_public(self):
    return {
      'url': self.url
    }
