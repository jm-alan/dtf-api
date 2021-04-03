from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .attending import attending
from .notification import notification
from .roster_entry import roster_entry

class User(db.Model, UserMixin):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  max_pins = db.Column(db.Integer, nullable=False)
  first_name = db.Column(db.String(40), nullable=False)
  default_locale = db.Column(db.String(255), nullable=True)
  hashed_password = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(255), nullable=False, unique=True)
  avatar_id = db.Column(db.Integer, db.ForeignKey('images.id'))

  avatar = db.relationship('Image', back_populates='users')
  hosted_events = db.relationship('Event', back_populates='host')
  comments = db.relationship('EventPost', back_populates='poster')
  sent_messages = db.relationship('Message', back_populates='sender')
  owned_convos = db.relationship('Conversation', back_populates='owner')
  attending_events = db.relationship('Event', secondary=attending)
  chatting_convos = db.relationship('Conversation', secondary=roster_entry)
  unread_conversations = db.relationship('Conversation', secondary=notification)


  @property
  def password(self):
    return self.hashed_password


  @password.setter
  def password(self, password):
    self.hashed_password = generate_password_hash(password)


  def check_password(self, password):
    return check_password_hash(self.password, password)


  def to_private(self):
    return {
      'id': self.id,
      'firstName': self.first_name,
      'email': self.email,
      'defaultLocale': self.default_locale,
      'maxPins': self.max_pins,
      'Avatar': self.avatar.to_public()
    }

  def to_public(self):
    return {
      'firstName': self.first_name,
      'Avatar': self.avatar.to_public()
    }
