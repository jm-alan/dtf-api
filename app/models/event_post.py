from .db import db

class EventPost(db.Model):
  __tablename__ = 'event_posts'

  id = db.Column(db.Integer, primary_key=True)
  author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
  body = db.Column(db.Text, nullable=False)

  author = db.relationship('User', back_populates='comments')
  event = db.relationship('Event', back_populates='comments')

  def to_public(self):
    return {
      'Author': self.author.to_public(),
      'body': self.body
    }
